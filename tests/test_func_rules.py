
from pytest import raises
from pythonrules import ruled, RuleViolationException

@ruled()
def f_func_rule(arg : lambda x : x == "abc"):
    pass

@ruled()
def f_func_rule_and_type(arg : (str, lambda x : x == "abc")):
    pass

def test_func_rule():
    f_func_rule("abc")
    with raises(RuleViolationException):
        f_func_rule("ab")

# checks only if functional rules work in tuples
def test_func_rule_and_type():
    f_func_rule_and_type("abc")
    with raises(RuleViolationException):
        f_func_rule_and_type("ab")