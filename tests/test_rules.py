
from pytest import raises
from pythonrules import ruled, LenRule, Rule
from pythonrules.exceptions import RuleViolationException

# TEST LenRule
@ruled()
def f_one_arg_str_len_eq(arg : LenRule(3)):
    pass

@ruled()
def f_one_arg_len_sm(arg : LenRule(3, "<")):
    pass

@ruled()
def f_one_arg_str_len_sm(arg : (str, LenRule(3, "<"))):
    pass

class TestLenRule:
    def test_one_arg_len_sq(self):
        f_one_arg_str_len_eq("abc")
        f_one_arg_str_len_eq([1, 2, 3])
        with raises(RuleViolationException):
            f_one_arg_str_len_eq("ab")

    def test_one_arg_len_sm_str(self):
        f_one_arg_str_len_sm("ab")
        with raises(RuleViolationException):
            f_one_arg_str_len_sm("abc")
        with raises(RuleViolationException):
            f_one_arg_str_len_sm([1, 2])
        with raises(RuleViolationException):
            f_one_arg_str_len_sm([1, 2, 3])


# TEST custom Rules
class PositiveNumRuleRet(Rule):
    def apply(self, value):
        if value < 0:
            return False

@ruled()
def f_one_arg_PNRRe(arg : PositiveNumRuleRet()):
    pass

class TestPositiveNumRuleRet:
    def test_one_arg_PNRRe(self):
        f_one_arg_PNRRe(2)
        with raises(RuleViolationException):
            f_one_arg_PNRRe(-1)

class PositiveNumRuleRet(Rule):
    def apply(self, value):
        if value < 0:
            raise RuleViolationException()

@ruled()
def f_one_arg_PNRRa(arg : PositiveNumRuleRet()):
    pass

class TestPositiveNumRuleRaise:
    def test_one_arg_PNRRa(self):
        f_one_arg_PNRRa(2)
        with raises(RuleViolationException):
            f_one_arg_PNRRa(-1)