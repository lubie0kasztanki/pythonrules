
from abc import ABC, abstractmethod
from typing import Dict, Union
from .exceptions import RuleViolationException


class Rule(ABC):
    '''Base class for all the rules.
       Subclass in order to define custom rules.'''
    @abstractmethod
    def apply(self, value: object, kwargs: Dict[str, object]) -> Union[bool, None]:
        pass


class LenRule(Rule):
    '''Rule for checking the length of iterable object.
       Uses built-in len function.'''

    def __init__(self, length: int, operator: str = "==") -> None:
        self.length = length
        self.operator = operator

    def fail(self, value: object) -> None:
        message = f"LenRule failed for length {self.length}, operarator {self.operator}, value {value}"
        raise RuleViolationException(message)

    def apply(self, value: object, kwargs: Dict[str, object] = None) -> None:
        if self.operator == "==":
            if len(value) != self.length:
                self.fail(value)
        elif self.operator == "<":
            if len(value) >= self.length:
                self.fail(value)
        elif self.operator == "<=":
            if len(value) > self.length:
                self.fail(value)
        elif self.operator == ">":
            if len(value) <= self.length:
                self.fail(value)
        elif self.operator == ">=":
            if len(value) < self.length:
                self.fail(value)
        else:
            raise ValueError()
