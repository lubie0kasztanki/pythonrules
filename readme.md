# Usage

Simply decorate your function with **@ruled()** and put rules as type hints.
Any time one of them gets violated a **RuleViolationException** will be thrown.

### Examples
```
# basic pep484 type checking
@ruled()
def f(x : int):
    pass

# type check, length check and combination
@ruled()
def g(x : str, y : LenRule(3, "=="), z : (str, LenRule(3, "=="))):
    pass
```