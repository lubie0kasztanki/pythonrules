
from pytest import raises
from pythonrules import ruled, Rule
from pythonrules.exceptions import RuleViolationException


class PositiveNumRuleRet(Rule):
    def apply(self, value, kwargs):
        if value < 0:
            return False

@ruled()
def f_custom_rule_with_return(arg : PositiveNumRuleRet()):
    pass

def test_custom_rule_with_return():
    f_custom_rule_with_return(2)
    with raises(RuleViolationException):
        f_custom_rule_with_return(-1)


class PositiveNumRuleRaise(Rule):
    def apply(self, value, kwargs):
        if value < 0:
            raise RuleViolationException()

@ruled()
def f_custom_rule_with_raise(arg : PositiveNumRuleRaise()):
    pass

def test_custom_rule_with_raise():
    f_custom_rule_with_raise(2)
    with raises(RuleViolationException):
        f_custom_rule_with_raise(-1)