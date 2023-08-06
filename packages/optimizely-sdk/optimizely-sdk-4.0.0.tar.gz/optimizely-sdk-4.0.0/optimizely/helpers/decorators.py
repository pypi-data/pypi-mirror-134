import warnings
import functools
import inspect


def deprecated_argument(parameter, reason):
    """ This is a decorator which can be used to mark a function parameter
    as deprecated. It will result in a warning being emitted when the
    function is used.

    Args:
        parameter: function parameter we want to deprecate.
        reason: A string describing the deprecation reason.

    Returns:
        Deprecation warning.
    """
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # get parameters of the decorated function
            params = inspect.signature(func)

            # map parameter names to arguments
            # In other words, map the passed `args`and `kwargs` to the function's signature
            bound_arguments = params.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            # get the value of the parameter in question
            value = bound_arguments.arguments.get(parameter)
            print('VALUE: ', value)

            if value is not None:
                warnings.simplefilter('always', DeprecationWarning)  # turn off filter
                warnings.warn(reason,
                              category=DeprecationWarning,
                              stacklevel=2)
                warnings.simplefilter('default', DeprecationWarning)  # reset filter
                return func(*args, **kwargs)
            return None
        return wrapper
    return inner


"""
1. not working if experiments_map old code runs or not

5. create a logger instead of printing to stdout
6. write tests for the decorator
7. will it work with all Py versions?
8. test
- works when different param is entered
- warning should not apply to other class properties, only to the specified parameter
"""

"""
Two issues:
1. decorator show in the opposite: when experiments_map is None!
2. warning shows already when "config.features_map" is called. Don't need to directly call experiments_map
 to trigger warning.

ASSUMPTION - we warn if experiment map exists or not. Not if it is called!!!!!
Experiment map exists, but we should be sending a warning if experiments_map is called.
We assumed that experiments_map being None in the init funciton means that experiments_map was not called!!! - WRONG!
We need to send warning if experiments_map call is made, Does that mean that's the same as experiments_map = None???
"""
