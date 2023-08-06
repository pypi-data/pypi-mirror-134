# IMPROVEMENT: This code is becoming a bit messy and hard to follow, due to some
# distinctions that are made between output and input (settings, and inputs) and
# the type of the arguments (mainly data frame versus non-data frame). We might
# need to rethink this a bit in the future.
import datetime as dt
from argparse import ArgumentParser

from balsam import selection
from balsam.store import DataFrameRef, JsonRef


def run_as_cli_program(task, args=None, store=None):
    """Runs the task as a command line program.

    :param task: The task to execute, should be an instance of
        :class:`~AbstractTask`.
    :param args: The list of command line arguments.  Ommit to use the actual
        command line arguments.
    :param store: The store to use to resolve references, such as
        :class:`~DataFrameRef` instances.

    :returns: The output of the task, the form of which is specified in the
              output schema of the task.
    """

    parser = create_argument_parser(task, no_output=False)
    if args is None:
        values = parser.parse_args()
    else:
        values = parser.parse_args(args)
    settings = _extract_keys(task.settings_schema.keys(), values)
    inputs = _extract_keys(task.input_schema.keys(), values)
    if store is not None:
        inputs = _resolve_inputs(store, inputs)
    output = task(settings, inputs)
    for key in task.output_schema:
        location = getattr(values, key)
        if hasattr(location, 'write'):
            location.write(output[key], store)
    return output


def _extract_keys(keys, values):
    result = {}
    for key in keys:
        result[key] = getattr(values, key)
    return result


def _resolve_inputs(store, inputs):
    result = {}
    for (key, value) in inputs.items():
        if hasattr(value, 'read'):
            result[key] = value.read(store)
        else:
            result[key] = value
    return result


class TaskArgumentParser(ArgumentParser):
    def __init__(self, task, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._task = task
        self._values = None

    def parse_args(self, *args, **kwargs):
        # pylint: disable=arguments-differ
        if not self._values:
            self._values = super().parse_args(*args, **kwargs)
        return self._values

    @property
    def settings(self):
        self.parse_args()
        return _extract_keys(self._task.settings_schema.keys(), self._values)


def create_argument_parser(task, *args, no_output=False, **kwargs):
    """Creates an argument parser for the task.

    Currently quite limited in what kind of task schemas it accepts.

    :param task: A task, i.e., something that complies with the :class:`~Task`
        interface.
    :param no_output: Do not parse output parameters.
    :param args, kwargs: They are passed directly to the constructor of the
        :class:`~ArgumentParser`.

    :returns: A Python argument parser.
    """
    parser = TaskArgumentParser(task, *args, **kwargs)
    _add_schema_to_group(parser, "settings", task.settings_schema)
    _add_schema_to_group(parser, "inputs", task.input_schema)
    if not no_output:
        _add_schema_to_group(
            parser, "outputs", task.output_schema, {'required': False}, is_output=True)
    return parser


def register_parser(type_desc, parser):
    """Registers a parser for atomic values."""
    _parsers[type_desc] = parser


_parsers = {
    'integer': int,
    'data_frame': DataFrameRef,
    'float': float,
    'date': lambda s: dt.datetime.strptime(s, '%Y-%m-%d').date(),
    'dict': JsonRef,
    'selection': lambda x: x
}


# TODO: clean this up
def _add_schema_to_group(parser, group_name, schema, overrides=None, is_output=False):
    group = parser.add_argument_group(group_name)
    overrides = overrides or {}

    for (name, field_schema) in schema.items():

        if field_schema.get('type') == 'list':
            overrides['required'] = overrides.get('required', True) and field_schema.get(
                'required', True)
            group.add_argument(
                "--{}".format(name),
                nargs='+',
                **_get_arguments(field_schema['schema'], overrides))
        elif field_schema.get('type') == 'data_frame' and is_output:
            group.add_argument(
                "--{}".format(name),
                **_get_arguments(field_schema, overrides),
                default=DataFrameRef("{}.csv".format(name)))
        elif field_schema.get('type') == 'dict' and is_output:
            group.add_argument(
                "--{}".format(name),
                **_get_arguments(field_schema, overrides),
                default=JsonRef("{}.json".format(name)))
        elif field_schema.get('type') == 'dict':
            group.add_argument("--{}".format(name), type=JsonRef, metavar='<json>')
        elif field_schema.get('type') == 'selection':
            overrides['required'] = overrides.get('required', True) and field_schema.get(
                'required', True)
            group.add_argument(
                "--{}".format(name), type=selection.parse, metavar='<json>')
        else:
            group.add_argument("--{}".format(name),
                               **_get_arguments(field_schema, overrides))

    return group


def _get_arguments(schema, overrides=None):
    arguments = {}
    if 'type' in schema:
        if schema['type'] in _parsers:
            arguments['type'] = _parsers[schema['type']]
            arguments['metavar'] = "<{}>".format(schema['type'])
        elif schema['type'] == 'boolean':
            arguments['action'] = 'store_true'
    arguments['required'] = schema.get('required', False)
    if 'allowed' in schema:
        arguments['choices'] = schema['allowed']
    for (key, value) in (overrides or {}).items():
        arguments[key] = value
    return arguments
