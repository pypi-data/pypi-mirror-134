from collections.abc import Iterator
from functools import wraps, partial
from typing import ParamSpec, TypeVar, Callable


__ALL__ = ['debug', 'debug_method']


P = ParamSpec('P')
T = TypeVar('T')
DecoratedFunc = Callable[[P], T]


def debug(func: DecoratedFunc | None = None, *,
          is_method: bool = False,
          intercept_iterators: bool = True) -> DecoratedFunc | Callable[[DecoratedFunc, bool, bool], DecoratedFunc]:

    if func is None:
        return partial(debug, is_method=is_method, intercept_iterators=intercept_iterators)

    @wraps(func)
    def wrapper(*args, **kwargs):
        output_args = f'({", ".join(map(repr, args if not is_method else args[1:]))}, ' \
                      f'{", ".join(f"{k}={v!r}" for k, v in kwargs.items())})'
        print(f'Called: {func.__qualname__}({output_args})')

        result = func(*args, **kwargs)
        print(f'{func.__qualname__} returned: {result!r}')

        if intercept_iterators and isinstance(result, Iterator):
            output = list(result)
            print(f"{func.__qualname__}:: returned: iter([{', '.join(repr(i) for i in output)}])")
            return iter(output)
        else:
            return result

    return wrapper


debug_method = partial(debug, is_method=True)
