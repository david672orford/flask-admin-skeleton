#! /usr/bin/env python3

import sys
import logging
from werkzeug.serving import run_simple
from werkzeug.middleware.proxy_fix import ProxyFix
from app import app

debug_mode = False
localhost = False
for arg in sys.argv[1:]:
	if arg == "--debug":
		debug_mode = True
	elif arg == "--localhost":
		localhost = True
	else:
		sys.stderr.write("Usage: %s [--debug] [--localhost]\n" % sys.argv[0])
		sys.exit(1)

logging.basicConfig(level=logging.DEBUG if debug_mode else logging.INFO)

if not debug_mode:
	from wsgi_door.providers import init_providers
	from wsgi_door.middleware import WsgiDoorAuth, WsgiDoorFilter
	app.wsgi_app = WsgiDoorFilter(app.wsgi_app, protected_paths=["/admin/"], allowed_groups=app.config["ALLOWED_GROUPS"])
	auth_providers = init_providers(app.config["AUTH_CLIENT_KEYS"])
	app.wsgi_app = WsgiDoorAuth(app.wsgi_app, auth_providers, app.config["SECRET_KEY"])

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_for=1)
run_simple("127.0.0.1" if localhost else "0.0.0.0", 5000, app, threaded=True)
