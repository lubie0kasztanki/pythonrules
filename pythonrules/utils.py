
def lookup_arg_names(func, args):
    '''Looks up names of all the arguments in args tuple.
       Merges them into kwargs dict.'''
    kwargs = {}
    for i in range(len(args)):
        kwargs[func.__code__.co_varnames[i]] = args[i]
    return kwargs 