import os
from enum import Enum
import logging
import json
from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

from balsam.store.encoder import CustomEncoder

log = logging.getLogger(__name__)


def create_ref(location, value):
    """Factory for :class:`~AbstractRef` instances.  The type of the instance
    depends on the data.

    :param location: Location the reference points to.  Does not include the
        extension.  This location is relative to some :class:`~RefStore`.
    :param value: The data for which the result should be a reference.
    """
    if isinstance(value, pd.DataFrame):
        return DataFrameRef(location + '.csv')
    if isinstance(value, np.ndarray):
        return ArrayRef(location + '.csv')
    if isinstance(value, (dict, str, int, float)):
        return JsonRef(location + '.json')
    raise ValueError("No reference for value of type '{}'".format(type(value)))


class Encoding(Enum):
    BINARY = 'b'
    STRING = ''


class AbstractRef(ABC):
    """
    Abstract base class for references, i.e., store-independent pointers to some
    data file.
    """

    def __init__(self, path):
        self.path = path

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.path == other.path

    @abstractmethod
    def parse(self, store):
        pass

    @abstractmethod
    def write(self, value, store):
        pass

    def read(self, store):
        return self.parse(store)

    def __hash__(self):
        return hash(self.path)

    def __repr__(self):
        return "<{}({})>".format(self.__class__.__name__, self.path)


class LoggedRefMixin:
    """Mixin for logging write and parse calls."""

    def parse(self, store):
        log.info('Reading %s from %s', self.path, store)

    def write(self, _value, store):
        log.info('Writing %s to %s', self.path, store)


class DataFrameRef(LoggedRefMixin, AbstractRef):
    """Reference to a pandas data frame."""

    def parse(self, store):
        """Reads the reference from the store.

        :param store: The store to read from.
        :returns: A data frame.
        """
        super().parse(store)
        sep = self._compute_seperator(self.path)

        with store.read(self.path) as handle:
            df = pd.read_csv(handle, sep=sep, header='infer', parse_dates=True)
            if 'date' in df.columns:
                log.info('Converting column to date')
                df['date'] = pd.to_datetime(
                    df['date'], infer_datetime_format=True).dt.date

            return df

    def write(self, value, store):
        """Writes the dataframe to the store.

        :param value: The data frame value to write.
        :param store: The store to write to.
        :returns: None
        """
        super().write(value, store)
        with store.write(self.path) as handle:
            value.to_csv(handle, index=False)

    @staticmethod
    def _compute_seperator(path):
        (_, ext) = os.path.splitext(path)
        if ext in ['.tsv']:
            return '\t'
        return ','


class JsonRef(LoggedRefMixin, AbstractRef):
    """Reference to a JSON file."""

    def parse(self, store):
        """Reads the reference from the store.

        :param stream: A store.
        :returns: A Python object.
        """
        super().parse(store)
        with store.read(self.path) as handle:
            value = json.load(handle)
            return self._read_arrays(value, store)

    def write(self, value, store):
        """Writes the JSON encoded value to buf.

        :param buf: The buf the write value to.
        :param value: The value to serialize.
        :returns: None
        """
        super().write(value, store)
        expanded = self._store_arrays(value, store)
        with store.write(self.path) as handle:
            json.dump(expanded, handle, cls=CustomEncoder)

    def _store_arrays(self, value, store):
        if isinstance(value, dict):
            expanded = value.copy()
            for (name, item) in value.items():
                if isinstance(item, pd.DataFrame):
                    (file_name, file_path) = self._create_array_file_name_and_path(
                        name, 'csv')
                    expanded[name] = file_name
                    DataFrameRef(file_path).write(item, store)
                if isinstance(item, np.ndarray):
                    (file_name, file_path) = self._create_array_file_name_and_path(
                        name, 'csv')
                    expanded[name] = file_name
                    ArrayRef(file_path).write(item, store)
            return expanded
        return value

    def _create_array_file_name_and_path(self, name, ext):
        file_name = '{name}.{ext}'.format(name=name, ext=ext)
        file_dir = os.path.dirname(self.path)
        return (file_name, os.path.join(file_dir, file_name))

    def _read_arrays(self, value, store):
        if isinstance(value, dict):
            for (name, item) in value.items():
                if self._is_csv(item):
                    value[name] = ArrayRef(item).read(store)
        return value

    def _is_csv(self, name):
        return hasattr(name, 'split') and name.split('.')[-1] == 'csv'


class ArrayRef(LoggedRefMixin, AbstractRef):
    """Reference to a file containing a numpy array."""

    def parse(self, store):
        super().parse(store)
        with store.read(self.path) as handle:
            return np.loadtxt(handle, delimiter=',')

    def write(self, value, store):
        super().write(value, store)
        with store.write(self.path) as handle:
            np.savetxt(handle, value, delimiter=',', fmt='%s')


class FileRef(LoggedRefMixin, AbstractRef):
    """Reference to either a text file or a binary file."""

    def __init__(self, path, encoding=Encoding.STRING):
        if not isinstance(encoding, Encoding):
            raise ValueError('encoding needs to be of type Encoding')
        super().__init__(path)
        self._encoding = encoding

    def parse(self, store):
        super().parse(store)
        with store.read(self.path, self._encoding) as handle:
            return handle.read()

    def write(self, value, store):
        super().write(value, store)
        with store.write(self.path, self._encoding) as handle:
            return handle.write(value)
