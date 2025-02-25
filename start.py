#! /usr/bin/env python3

from venv_tool import activate
activate()

import sys
import logging
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from werkzeug.serving import run_simple

parser = ArgumentParser(
	description = __doc__,
	formatter_class = RawDescriptionHelpFormatter,
	)
parser.add_argument("--debug", action="store_true")
parser.add_argument("--debug-requests", action="store_true")
parser.add_argument("--use-reloader", action="store_true")
parser.add_argument("--listen-addr", default="127.0.0.1")
parser.add_argument("--listen-port", type=int, default=5000)
options = parser.parse_args()

if options.debug:
	from app import app, start_background
	start_background()
else:
	from app.production import app

logging.basicConfig(level=logging.DEBUG if options.debug else logging.INFO)

if options.debug_requests:
	from http.client import HTTPConnection
	HTTPConnection.debuglevel = 1

run_simple(
	options.listen_address, options.listen_port,
	app,
	threaded=True,
	use_reloader = options.use_reloader,
	)
