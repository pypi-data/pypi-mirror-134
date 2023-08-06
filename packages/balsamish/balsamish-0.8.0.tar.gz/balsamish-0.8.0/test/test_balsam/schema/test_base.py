import numpy as np
import pandas as pd
import pytest

from balsam.schema import (ValidationError, array, check, data_frame, enum, integer,
                           list_of, dict_of, selection)
from balsam.selection import Contains, And, In


class BaseTestValidate:
    schema = None
    valid = None
    invalid = None

    def test_invalid_value_raises_error(self):
        with pytest.raises(ValidationError):
            check({"value": self.schema}, {"value": self.invalid})

    def test_valid_value_passes_check(self):
        try:
            check({"value": self.schema}, {"value": self.valid})
        except ValidationError as exc:
            assert False, exc


class TestValidateDataFrame(BaseTestValidate):
    schema = data_frame()
    valid = pd.DataFrame([1])
    invalid = []


class TestValidateInteger(BaseTestValidate):
    schema = integer()
    valid = 1
    invalid = "string"


class TestValidateEnum(BaseTestValidate):
    schema = enum(["x", "y"])
    valid = "x"
    invalid = "z"


class TestValidateArray(BaseTestValidate):
    schema = array()
    valid = np.array([1])
    invalid = [1]


class TestNonRequiredList(BaseTestValidate):
    schema = dict_of({'x': list_of(integer(), required=False)})
    valid = {}
    invalid = {'x': [1.2]}


class TestValidateSelection(BaseTestValidate):
    schema = selection()
    valid = And(In('campaignId', [1, 2, 3]), Contains('campaignText', 'nonBranded'))
    invalid = 'hello'
