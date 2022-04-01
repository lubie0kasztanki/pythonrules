
from pytest import raises
from pythonrules import ruled, RuleViolationException, LenRule


@ruled()
def f_one_arg_str_len_sm(arg : (str, LenRule(3, "<"))):
    pass


def test_one_arg_len_sm_str():
    f_one_arg_str_len_sm("ab")
    with raises(RuleViolationException):
        f_one_arg_str_len_sm("abc")
    with raises(RuleViolationException):
        f_one_arg_str_len_sm([1, 2])
    with raises(RuleViolationException):
        f_one_arg_str_len_sm([1, 2, 3])