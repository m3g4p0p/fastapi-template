import typing as t
from functools import update_wrapper

from starlette.datastructures import URL


def no_scheme_wrapper(url_for: t.Callable[..., URL]):
    def wrapper(*args, **kwargs):
        return url_for(*args, **kwargs).replace(scheme='')

    return update_wrapper(wrapper, url_for)
