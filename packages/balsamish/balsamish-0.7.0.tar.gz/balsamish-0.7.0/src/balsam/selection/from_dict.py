import inspect
from balsam.selection import base


def from_dict(obj):
    """Convert Python native object to a selection.

    :param obj: The object to convert
    :rtype: A selection, i.e., an instance of a subclass of :class:`~Selection`.
    """

    def _from_dict(_obj):
        if 'operation' in _obj:
            # Deserializes to a subclass of BinaryOperator
            for Op in _binary_operations():
                if Op.op == _obj['operation']:
                    try:
                        return Op(_from_dict(_obj['left']), _from_dict(_obj['right']))
                    except KeyError as exc:
                        raise ValueError("Could not convert {} to selection: {}".format(
                            obj, exc))
        if 'sql' in _obj:
            return base.SQL(_obj['sql'])
        return _obj

    conversion = _from_dict(obj)
    if not isinstance(conversion, base.Selection):
        raise ValueError("Could not convert {} to selection".format(obj))
    return conversion


def _binary_operations():
    for name in dir(base):
        item = getattr(base, name)
        if inspect.isclass(item) and issubclass(item, base.BinaryOperator):
            yield getattr(base, name)
        yield base.In
