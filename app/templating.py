from datetime import datetime
from typing import TypeVar

from fastapi.datastructures import URL
from fastapi.templating import Jinja2Templates
from jinja2 import Environment

from . import base_path
from .config import settings
from .enums import Mode
from .util import no_scheme_wrapper

T = TypeVar('T')


def with_version(url: URL):
    return url.include_query_params(
        version=settings.deta_space_app_version or
        str(datetime.now().timestamp()),
    )


templates = Jinja2Templates(
    base_path / 'templates',
)

jinja_env: Environment = templates.env
jinja_env.filters['with_version'] = with_version
jinja_env.globals['url_for'] = no_scheme_wrapper(
    templates.env.globals['url_for'])

if settings.mode is Mode.DEVELOP:
    jinja_env.add_extension('jinja2.ext.debug')
