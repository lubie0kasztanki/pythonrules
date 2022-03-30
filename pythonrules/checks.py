
from typing import Dict, List, Type, Union
from typeguard import check_type
from .rules import Rule
from .exceptions import RuleViolationException


def perform_type_check(value : object, type_ : Type) -> None:
    '''Checks if value is of certain type(generic or class).
       Raises RuleViolationException'''
    try:
        check_type("", value, type_)
    except:
        raise RuleViolationException(f"type missmatch expected {type_}\
                                      provided {type(value)}")


def perform_rule_check(func_name : str, kwargs : Dict[str, object], argname : str, rule : Union[Type, Rule]) -> None:
    '''Checks if argument comforms to a rule (type or Rule)
       Raises RuleViolationException with funcname and argname.'''
    value = kwargs[argname]
    if not isinstance(rule, Rule):
        try:
            perform_type_check(value, rule)
        except RuleViolationException as e:
            e.add_funcname_argname(func_name, argname)
            raise e
    else:
        try:
            if rule.apply(value) == False:
                raise RuleViolationException("Custom rule failed")
        except RuleViolationException as e:
            e.add_funcname_argname(func_name, argname)
            raise e


def check_rules(func_name : str, kwargs : Dict[str, object], annotations : List[Union[Type, Rule]]):
    '''Check of kwargs comform to their rule or rules set.
       Raises RuleViolationException with funcname and argname.'''
    for argname in kwargs:
        annotation = annotations[argname]
        if isinstance(annotation, tuple):
            for rule in annotation:
                perform_rule_check(func_name, kwargs, argname, rule)
        else:
            perform_rule_check(func_name, kwargs, argname, annotation)

