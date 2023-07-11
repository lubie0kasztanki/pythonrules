
class RuleViolationException(ValueError):
    '''Raised from failed Rule check or type check.
       Custom Rules should either raise this or return False in apply.'''
    def __init__(self, message : str="Rule violated") -> None:
        super().__init__(message)
        self.message = message

    def add_funcname_argname(self, funcname, argname) -> None:
        self.message = f"function {funcname}, argument {argname} {self.message}"
