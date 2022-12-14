from functools import wraps


def cosmetique(cosmetique_name):
    def cosmetique_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            print("|-------------------------|")
            print(f"|{cosmetique_name.center(25)}|")
            print("|-------------------------|")
            f = func(*args, **kwargs)
            print("|-------------------------|")
            return f
        return func_wrapper
    return cosmetique_decorator
