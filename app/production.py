from werkzeug.middleware.proxy_fix import ProxyFix
from wsgi_door.providers import init_providers
from wsgi_door.middleware import WsgiDoorAuth
import logging

from . import app

logger = logging.getLogger(__name__)
logger.info("Wrapping app in WSGI-Door")

app.wsgi_app = WsgiDoorAuth(app.wsgi_app, init_providers(app.config['AUTH_CLIENT_KEYS']), app.config['SECRET_KEY'])
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_for=1)

