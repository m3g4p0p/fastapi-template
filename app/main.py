from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from . import base_path
from .config import settings
from .templating import templates

app = FastAPI(title='Template')

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.secret_key,
)

app.mount('/static', StaticFiles(
    directory=base_path / 'static',
), 'static')


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.jinja', {
        'request': request,
    })
