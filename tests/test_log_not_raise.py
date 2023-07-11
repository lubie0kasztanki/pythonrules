
from pythonrules import ruled

@ruled(print)
def f_ruled_with_logging(arg : int):
    pass

EXPECTED_OUT = "function f_ruled_with_logging, argument arg type missmatch expected <class 'int'>, provided <class 'float'>\n"

def test_check_ruled_with_logging(capfd):
    f_ruled_with_logging(0.1)
    out, _ = capfd.readouterr()
    assert out == EXPECTED_OUT