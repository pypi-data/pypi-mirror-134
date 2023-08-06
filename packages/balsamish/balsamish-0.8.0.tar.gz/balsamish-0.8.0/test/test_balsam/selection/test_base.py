import pytest

from balsam.selection import List, In, Contains, And, Or, SQL, IContains


class TestSelectionToSql:
    @pytest.mark.parametrize('expr,sql',
                             [(List(1, 2, 3), '(1,2,3)'),
                              (In('helloId', [1, 2, 3]), '"helloId" in (1,2,3)'),
                              (Contains('name', 'sub'), '"name" like \'%%sub%%\''),
                              (And(In('id', [1, 2, 3]), In('pk', [4, 5, 6])),
                               '("id" in (1,2,3)) and ("pk" in (4,5,6))'),
                              (Or(In('id', [1, 2, 3]), In('pk', [4, 5, 6])),
                               '("id" in (1,2,3)) or ("pk" in (4,5,6))'),
                              (SQL('\"hello\" in (1, 2, 3)'), '\"hello\" in (1, 2, 3)'),
                              (IContains("name", "sub"), '"name" ilike \'%%sub%%\'')])
    def test_to_sql(self, expr, sql):
        assert expr.to_sql() == sql
