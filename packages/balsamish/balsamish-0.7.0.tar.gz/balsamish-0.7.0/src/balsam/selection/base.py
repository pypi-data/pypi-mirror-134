"""Contains a simple combinator language for predicates."""
import json
from abc import ABC, abstractmethod


def to_dict(selection):
    """Convert selection to an object that is built from Python native types.
    """
    if hasattr(selection, 'to_dict'):
        return selection.to_dict()
    return selection


def to_sql(selection):
    """
    Convert selection to a SQL condition (i.e., something that may be used in a
    where clause).
    """
    if hasattr(selection, 'to_sql'):
        return selection.to_sql()
    return str(selection)


def parse(_s):
    """Parse a selection. Currently not implemented.

    :param _s: The string to parse.
    """
    raise NotImplementedError()


class Selection(ABC):
    @abstractmethod
    def to_sql(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    def __repr__(self):
        return json.dumps(self.to_dict())


class List(Selection):
    def __init__(self, *elts):
        self._elts = elts

    def to_sql(self):
        return '({})'.format(','.join(to_sql(e) for e in self._elts))

    def to_dict(self):
        return list(self._elts)

    def __eq__(self, other):
        # pylint: disable=protected-access
        if isinstance(other, List):
            return other._elts == self._elts
        return False

    def __repr__(self):
        return repr(self._elts)


class BinaryOperator(Selection):
    op = None

    def __init__(self, left, right):
        self._left = left
        self._right = right

    @abstractmethod
    def to_sql(self):
        pass

    def to_dict(self):
        return {
            'left': to_dict(self._left),
            'operation': self.op,
            'right': to_dict(self._right)
        }

    def __eq__(self, other):
        # pylint: disable=protected-access
        if self.__class__ == other.__class__:
            return other._left == self._left and \
                other._right == self._right and \
                other.op == self.op
        return False

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, self._left, self._right)


class Contains(BinaryOperator):
    """Case sensitive substring match."""
    op = 'contains'

    def to_sql(self):
        # Need double % to distinguish from prinft interpolation prefix.
        return '\"{}\" like \'%%{}%%\''.format(to_sql(self._left), to_sql(self._right))


class And(BinaryOperator):

    op = 'and'

    def to_sql(self):
        return '({}) and ({})'.format(to_sql(self._left), to_sql(self._right))


class Or(BinaryOperator):
    op = 'or'

    def to_sql(self):
        return '({}) or ({})'.format(to_sql(self._left), to_sql(self._right))


class In(BinaryOperator):
    """List containment."""
    op = 'in'

    def __init__(self, left, right):
        super().__init__(left, right if isinstance(right, List) else List(*right))

    def to_sql(self):
        return '\"{}\" in {}'.format(to_sql(self._left), to_sql(self._right))

    def to_dict(self):
        return {
            'left': to_dict(self._left),
            'operation': self.op,
            'right': to_dict(self._right)
        }

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, self._left, self._right)


class IContains(BinaryOperator):
    """Case insensitive substring match."""
    op = 'icontains'

    def to_sql(self):
        # Need double % to distinguish from prinft interpolation prefix.
        return '\"{}\" ilike \'%%{}%%\''.format(to_sql(self._left), to_sql(self._right))


class SQL(Selection):
    """SQL literal."""

    def __init__(self, sql):
        self._sql = sql

    def to_sql(self):
        return self._sql

    def to_dict(self):
        return {"sql": self.to_sql()}

    def __eq__(self, other):
        # pylint: disable=protected-access
        if not isinstance(other, self.__class__):
            return False
        return other._sql == self._sql
