from enum import IntEnum
from abc import ABC, abstractmethod

from balsam.schema import check


class Check(IntEnum):
    """
    Enumeration to indicate to a task which of the settings, inputs and outputs
    to check.
    """
    NONE = 0x00
    SETTINGS = 0x01
    INPUT = 0x02
    OUTPUT = 0x04
    ALL = 0x07


class AbstractTask(ABC):
    """
    Interface definition for a task that takes two types of inputs: settings,
    and actual inputs, and returns output values.  A class implementing this
    interface is required to specify the schemas of all of its legal input and
    output values, i.e., to describe its (runtime) type as a function.
    """

    @property
    @abstractmethod
    def settings_schema(self):
        pass

    @property
    @abstractmethod
    def input_schema(self):
        pass

    @property
    @abstractmethod
    def output_schema(self):
        pass

    @abstractmethod
    def run(self, settings, inputs):
        pass

    def __call__(self, settings, inputs, checks=Check.SETTINGS | Check.INPUT):
        if Check.SETTINGS & checks:
            check(self.settings_schema, settings, {'task': self.__class__.__name__})
        if Check.INPUT & checks:
            check(self.input_schema, inputs, {'task': self.__class__.__name__})
        output = self.run(settings, inputs)
        if Check.OUTPUT & checks:
            check(self.output_schema, output, {'task': self.__class__.__name__})
        return output
