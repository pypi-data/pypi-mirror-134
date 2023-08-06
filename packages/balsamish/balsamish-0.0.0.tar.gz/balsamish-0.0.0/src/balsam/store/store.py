import io
import logging
import os
from abc import ABC, abstractmethod
from contextlib import contextmanager

import boto3

from balsam.store.refs import Encoding

log = logging.getLogger(__name__)


class AbstractRefStore(ABC):
    """
    Allows reading and writing of data via references.  Allows variation in two
    dimensions: the type of the data (e.g, a pandas data frame, or a native
    dictionary), and the storage location (e.g, an S3 bucket, or a local file
    system).
    """

    @abstractmethod
    @contextmanager
    def read(self, path, encoding):
        pass

    @abstractmethod
    @contextmanager
    def write(self, path, encoding):
        pass


class LocalRefStore(AbstractRefStore):
    def __init__(self, base_path=None):
        self._base_path = base_path

    @contextmanager
    def read(self, path, encoding=Encoding.STRING):
        """Provide a read only reference to the contents of the file at path.

        :param path: The location of the file to read.

        :returns: A read only stream (a file handle).
        """
        mode = 'rb' if encoding == Encoding.BINARY else 'r'
        with open(self._expand_path(path), mode) as handle:
            yield handle

    @contextmanager
    def write(self, path, encoding=Encoding.STRING):
        """Provide a write only reference to the file at path.

        :param path: The location of the file to read.

        :returns: A read only stream (a file handle).
        """
        full_path = self._expand_path(path)
        self._ensure_dir_exists(full_path)
        mode = 'wb' if encoding == Encoding.BINARY else 'w'
        with open(self._expand_path(path), mode) as handle:
            yield handle

    def _expand_path(self, path):
        if self._base_path is None:
            return path
        return os.path.join(self._base_path, path)

    @staticmethod
    def _ensure_dir_exists(full_path):
        try:
            os.makedirs(os.path.dirname(full_path))
        except OSError:
            pass

    def __repr__(self):
        return '<{}({})>'.format(self.__class__.__name__, self._base_path)


class InMemoryRefStore(AbstractRefStore):
    """Reference store that keeps data in memory."""

    def __init__(self):
        self._data = {}

    @contextmanager
    def write(self, path, encoding=Encoding.STRING):
        resource = io.StringIO()
        yield resource
        resource.seek(0)
        self._data[path] = resource.read()

    @contextmanager
    def read(self, path, encoding=Encoding.STRING):
        yield io.StringIO(self._data[path])

    def read_raw(self, path):
        return self._data.get(path)

    def write_raw(self, path, contents):
        self._data[path] = contents

    def __repr__(self):
        return '<{}()>'.format(self.__class__.__name__)


class RemoteRefStoreS3(AbstractRefStore):
    """Reference store that puts data on S3."""

    # Reuse the client over multiple puts and gets
    _client = None

    def __init__(self, bucket, prefix, config=None):
        """Instantiate a ReferenceStore that puts its data on S3.

        :param bucket: The bucket to store data in.
        :param prefix: The prefix within that bucket, under which to store data.
        :param config: Additional configuration passed to the boto3 client
            constructor.  This might include, `aws_key_id` and
            `aws_secret_access_key`.

        :returns: Instance of a subclass of :class:`~AbstractRefStore`.
        """

        self._bucket = bucket
        self._prefix = prefix
        self._config = self._extract_config(config)

    @classmethod
    def _extract_config(cls, config):
        if not config:
            return {}
        result = {}
        for key in ['aws_access_key_id', 'aws_secret_access_key']:
            if key in config:
                result[key] = config[key]
        return result

    @property
    def s3(self):
        if self._client is None:
            log.info('Creating S3 client with access key ID: %s',
                     self._config.get('aws_access_key_id'))
            self._client = boto3.client('s3', **self._config)
        return self._client

    @contextmanager
    def read(self, path, encoding=Encoding.STRING):
        key = self._expand_path(path)
        response = self.s3.get_object(Bucket=self._bucket, Key=key)
        yield response['Body']

    @contextmanager
    def write(self, path, encoding=Encoding.STRING):
        resource = ChimearicIO()
        yield resource
        resource.seek(0)
        key = self._expand_path(path)
        self.s3.put_object(Body=resource, Bucket=self._bucket, Key=key)

    def _expand_path(self, path):
        return os.path.join(self._prefix, path)

    def __repr__(self):
        return '<{}({}:{})>'.format(self.__class__.__name__, self._bucket, self._prefix)


class ChimearicIO(io.BytesIO):
    """BytesIO wrapper that additionally takes care of encoding strings before
    writing them to the bytes buffer.
    """

    def write(self, s):
        if isinstance(s, str):
            super().write(s.encode('utf8'))
        else:
            super().write(s)
