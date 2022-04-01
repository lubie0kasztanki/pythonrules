
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
def f_multi_arg_int(arg1 : int, arg2 : int):
    pass

@ruled()
def f_one_arg_list_int(arg : List[int]):
    pass

@ruled()
def f_multi_arg_list_int(arg1 : List[int], arg2 : List[int]):
    pass

@ruled()
def f_multi_arg_mixed(arg1 : int, arg2 : List[int]):
    pass

class TestTypes:

    @ruled()
    def m_one_arg_int(self, arg : int):
        pass

    def test_one_arg_int(self):
        f_one_arg_int(1)
        self.m_one_arg_int(1)
        with raises(RuleViolationException):
            f_one_arg_int("x")
        with raises(RuleViolationException):
            self.m_one_arg_int("x")
        with raises(RuleViolationException):
            f_one_arg_int(custom_obj)
        with raises(RuleViolationException):
            self.m_one_arg_int(custom_obj)
        with raises(RuleViolationException):
            f_one_arg_int(0.5)
        with raises(RuleViolationException):
            self.m_one_arg_int(0.5)

    def test_multi_arg_int(self):
        f_multi_arg_int(1, 2)
        with raises(RuleViolationException):
            f_multi_arg_int("x", 1)
        with raises(RuleViolationException):
            f_multi_arg_int(1, custom_obj)
        with raises(RuleViolationException):
            f_multi_arg_int(0.5, 3)

    def test_one_arg_list_int(self):
        f_one_arg_list_int([1, 2, 3])
        f_one_arg_list_int([])
        with raises(RuleViolationException):
            f_one_arg_list_int(["abc"])
        with raises(RuleViolationException):
            f_one_arg_list_int(1)
        with raises(RuleViolationException):
            f_one_arg_list_int(custom_obj)

    def test_multi_arg_list_int(self):
        f_multi_arg_list_int([1, 2, 3], [1, 2])
        f_multi_arg_list_int([], [1,2])
        with raises(RuleViolationException):
            f_multi_arg_list_int(["abc"], [])
        with raises(RuleViolationException):
            f_multi_arg_list_int([1, 2, 3], ["abc"])
        with raises(RuleViolationException):
            f_multi_arg_list_int(custom_obj, 1)

    def test_multi_arg_mixed(self):
        f_multi_arg_mixed(1, [1, 2, 3])
        with raises(RuleViolationException):
            f_multi_arg_mixed("abc", [1, 2, 3])
        with raises(RuleViolationException):
            f_multi_arg_mixed("abc", [1, 2, 3])    
        with raises(RuleViolationException):
            f_multi_arg_mixed(1, 1)