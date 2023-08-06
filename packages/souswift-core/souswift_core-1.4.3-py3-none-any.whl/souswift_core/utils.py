import asyncio
import warnings
from functools import wraps
from typing import Callable, TypeVar

from typing_extensions import ParamSpec

T = TypeVar('T')
P = ParamSpec('P')


def deprecated(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        warnings.warn(
            f'{func.__name__} is deprecated and can be removed without notice!',
            DeprecationWarning,
        )
        return func(*args, **kwargs)

    return inner


async def as_async(
    func: Callable[P, T], *args: P.args, **kwargs: P.kwargs
) -> T:
    """Asynchronously schedule sync function to run in a separate thread"""
    return await asyncio.to_thread(func, *args, **kwargs)
