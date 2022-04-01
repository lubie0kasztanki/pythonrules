
from pytest import raises
from pythonrules import ruled, RuleViolationException
from pythonrules.rules import Rule

@ruled()
def f_one_arg_func_rule_no_kw(arg : lambda x : x == "abc"):
    pass

@ruled()
def f_one_arg_str_func_rule_no_kw(arg : (str, lambda x : x == "abc")):
    pass

def test_one_arg_func_rule_no_kw():
    f_one_arg_func_rule_no_kw("abc")
    with raises(RuleViolationException):
        f_one_arg_func_rule_no_kw("ab")

def test_one_arg_str_func_rule_no_kw():
    f_one_arg_str_func_rule_no_kw("abc")
    with raises(RuleViolationException):
        f_one_arg_str_func_rule_no_kw(2)
    with raises(RuleViolationException):
        f_one_arg_str_func_rule_no_kw("ab")