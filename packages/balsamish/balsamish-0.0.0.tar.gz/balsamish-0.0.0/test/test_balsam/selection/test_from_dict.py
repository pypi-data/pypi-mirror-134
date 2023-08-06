import pytest
from balsam.selection import from_dict, to_dict
from balsam.selection import Contains, In, And, Or, SQL, IContains


@pytest.mark.parametrize(
    'selection',
    [(Contains('x', 'y')), (In('x', [1, 2, 3])), (And(In('x', 'y'), Contains('u', 'v'))),
     (Or(In('x', 'y'), Contains('u', 'v'))),
     (And(Or(In('x', 'y'), Contains('u', 'v')), And(In('x', 'y'), Contains('u', 'v')))),
     (SQL('"name" in (1, 2, 3)')), (IContains('x', 'y'))])
def test_to_dict_then_from_dict_is_id(selection):
    assert from_dict(to_dict(selection)) == selection


@pytest.mark.parametrize('obj,expected', [({
    'operation': 'in',
    'left': 'campaignId',
    'right': [1, 2, 3]
}, In('campaignId', [1, 2, 3]))])
def test_from_dict_conversion_directl(obj, expected):
    assert from_dict(obj) == expected


@pytest.mark.parametrize('obj', [({'operation': 'in'}, 'hello')])
def test_from_dict_throws_value_error_on_failure(obj):
    with pytest.raises(ValueError):
        from_dict(obj)
