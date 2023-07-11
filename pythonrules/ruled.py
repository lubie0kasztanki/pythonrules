
from .exceptions import RuleViolationException
from .utils import lookup_arg_names
from .checks import check_rules

def ruled(logger=None):
    '''Decorator for all the PythonRuled functions'''
    def _ruled(func):
        func_name = func.__name__
        func_annotations = func.__annotations__
        _logger = logger
        def ruled_wrapped(*args, **kwargs):
            args_dict = lookup_arg_names(func, args)
            for name in args_dict:
                kwargs[name] = args_dict[name]
            try:
                check_rules(func_name, kwargs, func_annotations)
            except RuleViolationException as e:
                if logger != None:
                    _logger(e.message)
                else:
                    raise e
            return func(**kwargs)
        return ruled_wrapped
    return _ruled
