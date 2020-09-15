import functools


class clr:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        print(f"\n================================================")
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        fname = f"{clr.BLUE}{clr.BOLD}{func.__name__!r}{clr.ENDC}"
        print(
            f"{clr.GREEN}[Calling]{clr.ENDC} {fname} {clr.WARNING}{func.__name__}({signature}){clr.ENDC}")
        value = func(*args, **kwargs)
        # 4
        print(
            f"{clr.GREEN}[return]{clr.ENDC} {fname} {clr.WARNING}returned {value!r}{clr.ENDC}")
        return value
    return wrapper_debug
