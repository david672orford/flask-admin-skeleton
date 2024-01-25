from flask import Flask
import sys

app = Flask(__name__, instance_relative_config=True)
default_config = dict(
	APP_DISPLAY_NAME = "Flask Admin Skeleton",
	SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/app.db' % app.instance_path,
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
	SQLALCHEMY_ECHO = False,
	FLASK_ADMIN_FLUID_LAYOUT = True,
	FLASK_ADMIN_SWATCH = 'cerulean',
	SECRET_KEY = None,
	)
app.config.from_mapping(**default_config)
app.config.from_pyfile('config.py')

error_count = 0
for item in default_config.keys():
	if app.config[item] is None:
		sys.stderr.write("ERROR: Required configuration item %s is not defined\n" % item)
		error_count += 1
if error_count > 0:
	sys.exit(1)

from . import admin
from . import views

