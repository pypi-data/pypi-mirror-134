import datetime as dt

import pandas as pd
import pytest

from balsam.schema import (ValidationError, boolean, data_frame, date, dict_of, enum,
                           floating, integer, list_of)
from balsam.store import DataFrameRef, InMemoryRefStore, JsonRef, LocalRefStore
from balsam.tasks import AbstractTask, create_argument_parser, run_as_cli_program
from test_balsam.utils import expand_path


@pytest.fixture
def mock_store():
    return InMemoryRefStore()


@pytest.fixture
def ref_store():
    return LocalRefStore()


@pytest.fixture
def df():
    """Return the content of the `df.csv` fixture as a data frame."""
    return pd.DataFrame({1: [3], 2: [4]})


class TestRunAsCliProgram:
    def test_inputs_are_passed_to_task(self):
        task = _create_test_task({'initial': integer()}, {})
        output = run_as_cli_program(task, '--initial 1'.split())
        assert output == {'input/initial': 1}

    def test_settings_are_passed_to_task(self):
        task = _create_test_task({}, {'iterations': integer()})
        output = run_as_cli_program(task, '--iterations 100'.split())
        assert output == {'settings/iterations': 100}

    def test_does_not_load_data_frame_without_store(self):
        task = _create_test_task({'data': data_frame()}, {})
        with pytest.raises(ValidationError):
            run_as_cli_program(task, ['--data', expand_path('df.csv')])

    def test_load_data_frame_with_store(self, mock_store):
        task = _create_test_task({'data': data_frame()}, {})
        df = pd.DataFrame([1])
        DataFrameRef('df.csv').write(df, mock_store)

        output = run_as_cli_program(task, '--data df.csv'.split(), mock_store)
        assert (output['input/data'].values == df.values).all()

    def test_input_parameters_are_required_by_default(self, mock_store):
        task = _create_test_task({'data': data_frame()}, {})
        with pytest.raises(SystemExit):
            run_as_cli_program(task, [], mock_store)

    def test_settings_parameters_are_required_by_default(self, mock_store):
        task = _create_test_task({}, {'iterations': integer()})
        with pytest.raises(SystemExit):
            run_as_cli_program(task, [], mock_store)

    def test_arbitrary_output_params_are_not_required(self, mock_store):
        task = _create_test_task({}, {}, {'out': integer()})
        try:
            run_as_cli_program(task, [], mock_store)
        except SystemExit as exc:
            assert False, exc

    def test_data_frame_output_params_values_have_defaults(self, mock_store):
        task = _create_test_task({'df': data_frame()}, {}, {'input/df': data_frame()})
        expected = pd.DataFrame([1])
        DataFrameRef('in.csv').write(expected, mock_store)

        run_as_cli_program(task, '--df in.csv'.split(), mock_store)

        actual = DataFrameRef('input/df.csv').parse(mock_store)
        assert actual.values == expected.values

    def test_data_frame_outputs_are_written_to_store(self, mock_store):
        task = _create_test_task({'df': data_frame()}, {}, {'input/df': data_frame()})
        expected = pd.DataFrame([1])
        DataFrameRef('in.csv').write(expected, mock_store)

        run_as_cli_program(task, '--df in.csv --input/df out.csv'.split(), mock_store)

        actual = DataFrameRef('out.csv').parse(mock_store)
        assert actual.values == expected.values

    def test_json_outputs_are_written_to_store(self, mock_store):
        task = _create_output_task({
            'result': dict_of({
                'count': integer()
            })
        }, {'result': {
            'count': 1
        }})
        run_as_cli_program(task, '--result file.json'.split(), mock_store)

        assert JsonRef('file.json').parse(mock_store) == {'count': 1}

    def test_json_inputs_are_read_from_store(self, mock_store):
        value = {'count': 1}
        task = _create_test_task({'data': dict_of({'count': integer()})}, {})
        JsonRef('file.json').write(value, mock_store)
        output = run_as_cli_program(task, '--data file.json'.split(), mock_store)
        assert output['input/data'] == value


class TestCreateCommandLineParser:
    def test_parse_integers(self):
        task = _create_test_task({'initial': integer()}, {'count': integer()})
        parser = create_argument_parser(task)
        values = parser.parse_args(['--initial', '0', '--count', '1'])
        assert values.initial == 0
        assert values.count == 1

    def test_parse_list_of_integers(self):
        task = _create_test_task({'initial': list_of(integer())}, {'count': integer()})
        parser = create_argument_parser(task)
        values = parser.parse_args('--initial 0 1 2 --count 1'.split())
        assert values.initial == [0, 1, 2]
        assert values.count == 1

    def test_parse_data_frame_reference(self):
        task = _create_test_task({}, {'df': data_frame()})
        parser = create_argument_parser(task)
        values = parser.parse_args('--df data.csv'.split())
        assert values.df == DataFrameRef('data.csv')

    def test_parse_floating_point(self):
        task = _create_test_task({}, {'real': floating()})
        parser = create_argument_parser(task)
        values = parser.parse_args('--real 0.9'.split())
        assert values.real == 0.9

    def test_parse_enum(self):
        task = _create_test_task({}, {'value': enum(["x", "y"])})
        parser = create_argument_parser(task)
        values = parser.parse_args('--value x'.split())
        assert values.value == "x"

    def test_parse_dict_as_json_ref(self):
        task = _create_test_task({}, {'json': dict_of({'n': integer()})}, {})
        parser = create_argument_parser(task)
        values = parser.parse_args('--json file.json'.split())
        assert values.json == JsonRef('file.json')

    def test_use_default_value_when_json_ref_is_missing(self):
        task = task = _create_test_task({}, {}, {'results': dict_of({'n': integer()})})
        parser = create_argument_parser(task)
        values = parser.parse_args([])
        assert values.results == JsonRef('results.json')

    def test_parse_enum_fails_when_argument_not_allowed(self):
        task = _create_test_task({}, {'value': enum(["x", "y"])})
        parser = create_argument_parser(task)
        with pytest.raises(SystemExit):
            parser.parse_args('--value z'.split())

    def test_parse_presence_of_flag_as_true(self):
        task = _create_test_task({}, {'flag': boolean()})
        parser = create_argument_parser(task)
        value = parser.parse_args(['--flag'])
        assert value.flag is True

    def test_parse_absence_of_flag_as_false(self):
        task = _create_test_task({}, {'flag': boolean()})
        parser = create_argument_parser(task)
        value = parser.parse_args([])
        assert value.flag is False

    def test_parse_date(self):
        task = _create_test_task({}, {'date': date()})
        parser = create_argument_parser(task)
        value = parser.parse_args('--date 2019-01-01'.split())
        assert value.date == dt.date(2019, 1, 1)


def _create_test_task(input_schema, settings_schema, output_schema=None):
    class TestTask(AbstractTask):
        @property
        def input_schema(self):
            return input_schema

        @property
        def output_schema(self):
            return output_schema or {}

        @property
        def settings_schema(self):
            return settings_schema

        def run(self, settings, inputs):
            result = {}
            for (key, value) in settings.items():
                result['settings/{}'.format(key)] = value
            for (key, value) in inputs.items():
                result['input/{}'.format(key)] = value
            return result

    return TestTask()


def _create_output_task(output_schema, output):
    class OutputTestTask(AbstractTask):
        @property
        def input_schema(self):
            return {}

        @property
        def output_schema(self):
            return output_schema

        @property
        def settings_schema(self):
            return {}

        def run(self, _settings, _inputs):
            return output

    return OutputTestTask()
