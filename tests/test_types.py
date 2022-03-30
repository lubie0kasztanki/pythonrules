
from typing import List
from pytest import raises
from pythonrules import ruled
from pythonrules.exceptions import RuleViolationException


class CustomClass:
    pass
custom_obj = CustomClass()

@ruled()
def f_one_arg_int(arg : int):
    pass

@ruled()
def f_one_arg_list_int(arg : List[int]):
    pass


def test_one_arg_int():
    f_one_arg_int(1)
    with raises(RuleViolationException):
        f_one_arg_int("x")
    with raises(RuleViolationException):
        f_one_arg_int(custom_obj)
    with raises(RuleViolationException):
        f_one_arg_int(0.5)

def test_one_arg_list_int():
    f_one_arg_list_int([1, 2, 3])
    f_one_arg_list_int([])
    with raises(RuleViolationException):
        f_one_arg_list_int(["abc"])
    with raises(RuleViolationException):
        f_one_arg_list_int(1)
    with raises(RuleViolationException):
        f_one_arg_list_int(custom_obj)



