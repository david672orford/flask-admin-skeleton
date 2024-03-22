#! /usr/bin/env python3

import sys, logging
from werkzeug.serving import run_simple

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

if debug_mode:
	from app import app
else:
	from app.production import app

logging.basicConfig(level=logging.DEBUG if debug_mode else logging.INFO)

run_simple("127.0.0.1" if localhost else "0.0.0.0", 5000, app, threaded=True)
