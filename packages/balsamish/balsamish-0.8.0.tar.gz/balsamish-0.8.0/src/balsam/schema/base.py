import cerberus


class ValidationError(Exception):
    """Exception thrown when validation fails."""

    def __init__(self, document, errors, info=None):
        super().__init__(self, "Failed to validate")
        self.errors = errors
        self.info = info
        self._document = document

    def __repr__(self):
        if self.info:
            return "<{}({}, {}, {})>".format(self.__class__.__name__, self._document,
                                             self.errors, self.info)
        return "<{}({}, {})>".format(self.__class__.__name__, self._document,
                                     self.errors)


def check(schema, document, info=None):
    """Validates whether the document complies with the schema.  Aims to
    abstract away some details of the schema library from the client.

    :param schema: A schema constructed from balsam types.
    :param document: The value to check against the schema.

    :raises ValidationError: When the document does not comply with the schema.

    :returns: The document.
    """
    v = cerberus.Validator(schema, allow_unknown=True)
    if not v.validate(document):
        raise ValidationError(document, v.errors, info)
    return document


def integer(required=True):
    return {'required': required, 'type': 'integer'}


def list_of(schema, required=True):
    nullable = not required
    return {'type': 'list', 'required': required, 'nullable': nullable, 'schema': schema}


def data_frame():
    return {'required': True, 'type': 'data_frame'}


def date():
    return {'required': True, 'type': 'date'}


def string(required=True):
    return {'required': required, 'type': 'string'}


def floating():
    return {'required': True, 'type': 'float'}


def enum(values):
    return {'required': True, 'type': 'string', 'allowed': values}


def boolean():
    return {'type': 'boolean'}


def dict_of(schema, required=True):
    nullable = not required
    return {'type': 'dict', 'required': required, 'nullable': nullable, 'schema': schema}


def array():
    return {'required': True, 'type': 'array'}


def datetime(required=True):
    nullable = not required
    return {'required': required, 'nullable': nullable, 'type': 'datetime'}


def selection(required=True):
    nullable = not required
    return {'required': required, 'nullable': nullable, 'type': 'selection'}
