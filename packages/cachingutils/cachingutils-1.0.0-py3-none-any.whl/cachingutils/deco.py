from functools import wraps
from typing import Any, Awaitable, Callable, ParamSpec, Sequence, TypeVar

from .cache import Cache

P = ParamSpec("P")
T = TypeVar("T")


def _extend_posargs(sig: list, posargs: list[int], *args) -> None:
    for i in posargs:
        val = args[i]

        hashed = hash(val)

        sig.append(hashed)


def _extend_kwargs(sig: list, _kwargs: list[str], **kwargs) -> None:
    for name in _kwargs:
        val = kwargs[name]

        hashed = hash(val)

        sig.append(hashed)


def _get_sig(
    include_posargs: list[int] = None, include_kwargs: list[str] = None, *args, **kwargs
) -> Sequence[int]:
    signature = []

    if include_posargs:
        _extend_posargs(signature, include_posargs, *args)

    if include_kwargs:
        _extend_kwargs(signature, include_kwargs, **kwargs)

    return tuple(signature)


def cached(
    timeout: float = None,
    include_posargs: list[int] = None,
    include_kwargs: list[str] = None,
    cache: Cache = None,
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    _cache: Cache[Sequence[int], Any] = cache or Cache(timeout=timeout)

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            sig = _get_sig(include_posargs, include_kwargs, *args, **kwargs)

            if value := _cache.get(sig):
                return value

            retval = func(*args, **kwargs)

            _cache[sig] = retval

            return retval

        return wrapper

    return decorator


def acached(
    timeout: float = None,
    include_posargs: list[int] = None,
    include_kwargs: list[str] = None,
    cache: Cache = None,
) -> Callable[[Callable[P, Awaitable[T]]], Callable[P, Awaitable[T]]]:
    _cache: Cache[Sequence[int], Any] = cache or Cache(timeout=timeout)

    def decorator(func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
        @wraps(func)
        async def awrapper(*args, **kwargs) -> T:
            sig = _get_sig(include_posargs, include_kwargs, *args, **kwargs)

            if value := _cache.get(sig):
                return value

            retval: T = await func(*args, **kwargs)

            _cache[sig] = retval

            return retval

        return awrapper

    return decorator
