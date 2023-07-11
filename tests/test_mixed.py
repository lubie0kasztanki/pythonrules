
""" Checks if all of the rules in a tuple work. """

from pytest import raises
from pythonrules import ruled, RuleViolationException, LenRule


@ruled()
def f_type_and_LenRule(arg : (str, LenRule(3, "<"))):
    pass

def test_type_and_LenRule():
    f_type_and_LenRule("ab")
    with raises(RuleViolationException):
        f_type_and_LenRule("abc")
    with raises(RuleViolationException):
        f_type_and_LenRule([1, 2])
    with raises(RuleViolationException):
        f_type_and_LenRule([1, 2, 3])