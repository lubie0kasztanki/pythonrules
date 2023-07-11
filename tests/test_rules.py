
from pytest import raises
from pythonrules import ruled, LenRule, Rule
from pythonrules.exceptions import RuleViolationException

# TEST LenRule
@ruled()
def f_LenRule_default(arg : LenRule(3)):
    pass

def test_LenRule_default():
    f_LenRule_default("abc")
    f_LenRule_default([1, 2, 3])
    with raises(RuleViolationException):
        f_LenRule_default("ab")

@ruled()
def f_LenRule_st(arg : LenRule(3, "<")):
    pass

def test_LenRule_st():
    f_LenRule_st("ab")
    f_LenRule_st([1])
    with raises(RuleViolationException):
        f_LenRule_st("abc")
