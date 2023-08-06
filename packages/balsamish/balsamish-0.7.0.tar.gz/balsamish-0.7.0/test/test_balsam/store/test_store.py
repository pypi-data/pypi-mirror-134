# pylint: disable=no-self-use
import json
import os
import uuid

import numpy as np
import pandas as pd
import pytest

from balsam.store import (ArrayRef, DataFrameRef, Encoding, FileRef, InMemoryRefStore,
                          JsonRef, LocalRefStore)
from test_balsam.utils import expand_path


@pytest.fixture
def store():
    return LocalRefStore()


@pytest.fixture
def mock_store():
    return InMemoryRefStore()


class TestLocalRefStore:
    def test_reading_data_frames(self, store):
        ref = DataFrameRef(expand_path('df.csv'))
        df = ref.parse(store)
        assert isinstance(df, pd.DataFrame)

    def test_write_binary_data(self, store):
        path = f'{uuid.uuid4()}.bin'
        try:
            ref = FileRef(path, encoding=Encoding.BINARY)
            ref.write(b'xxx', store)
            value = ref.read(store)
            assert value == b'xxx'
        finally:
            os.remove(path)

    def test_write_string_data(self, store):
        path = f'{uuid.uuid4()}.bin'
        try:
            ref = FileRef(path, encoding=Encoding.STRING)
            ref.write('xxx', store)
            value = ref.read(store)
            assert value == 'xxx'
        finally:
            os.remove(path)


class TestDataFrameRef:
    def test_write_data_frame_to_buffer(self, store):
        df = pd.DataFrame([1])
        path = expand_path('not_used.csv')
        ref = DataFrameRef(path)
        ref.write(df, store)

        actual = pd.read_csv(path, index_col=0)
        os.remove(path)

        assert (actual.values == df.values).all()

    def test_read_csv_data_frame_ref(self, mock_store):
        ref = DataFrameRef('df.csv')
        expected = pd.DataFrame({'x': [1], 'y': [2]})
        ref.write(expected, mock_store)

        actual = ref.read(mock_store)
        assert actual.equals(expected)

    def test_read_tsv_data_frame_ref(self, mock_store):
        mock_store.write_raw('df.tsv', 'x\ty\n1\t2')
        ref = DataFrameRef('df.tsv')
        expected = pd.DataFrame({'x': [1], 'y': [2]})

        actual = ref.read(mock_store)
        assert actual.equals(expected)


class TestJsonRef:
    def test_storing_json_values(self, mock_store):
        ref = JsonRef('single.json')
        ref.write({'x': 1}, mock_store)
        assert ref.read(mock_store) == {'x': 1}

    def test_storing_json_values_with_data_frames(self, mock_store):
        ref = JsonRef('compound.json')
        df1 = pd.DataFrame([1])
        df2 = pd.DataFrame([2])
        ref.write({'df1': df1, 'df2': df2}, mock_store)

        assert (DataFrameRef('df1.csv').read(mock_store).values == df1.values).all()
        assert (DataFrameRef('df2.csv').read(mock_store).values == df2.values).all()
        assert json.loads(mock_store.read_raw('compound.json')) == {
            'df1': 'df1.csv',
            'df2': 'df2.csv'
        }

    def test_storing_json_values_with_arrays(self, mock_store):
        ref = JsonRef('compound.json')
        arr1 = np.array([1, 2])
        arr2 = np.array([3, 4])
        ref.write({'arr1': arr1, 'arr2': arr2}, mock_store)

        assert (ArrayRef('arr1.csv').read(mock_store) == arr1).all()
        assert (ArrayRef('arr2.csv').read(mock_store) == arr2).all()
        assert json.loads(mock_store.read_raw('compound.json')) == {
            'arr1': 'arr1.csv',
            'arr2': 'arr2.csv'
        }

    def test_store_values_references_in_json_in_same_dir(self, mock_store):
        ref = JsonRef('dir/compound.json')
        arr1 = np.array([1, 2])
        ref.write({'arr1': arr1}, mock_store)

        assert (ArrayRef('dir/arr1.csv').read(mock_store) == arr1).all()

    def test_reading_json_values(self, mock_store):
        ref = JsonRef('single.json')
        ref.write({'x': 1}, mock_store)
        assert ref.read(mock_store) == {'x': 1}

    def test_reading_json_values_with_references(self, mock_store):
        ref = JsonRef('compound.json')
        ref.write({'arr1': 'array1.csv', 'arr2': 'array2.csv'}, mock_store)
        arr1 = np.array([1, 2])
        arr2 = np.array([3, 4])
        arr1_ref = ArrayRef('array1.csv')
        arr2_ref = ArrayRef('array2.csv')
        arr1_ref.write(arr1, mock_store)
        arr2_ref.write(arr2, mock_store)

        actual = ref.read(mock_store)
        assert set(actual.keys()) == {'arr1', 'arr2'}
        assert (actual['arr1'] == arr1).all()
        assert (actual['arr2'] == arr2).all()
