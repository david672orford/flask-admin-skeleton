from app import app
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.engine import Engine
from sqlalchemy import event

db = SQLAlchemy(app)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
	cursor = dbapi_connection.cursor()
	cursor.execute("PRAGMA foreign_keys=ON")
	cursor.close()

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	handle = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	def __str__(self):
		return "{handle} <{email}>".format(handle=self.handle, email=self.email)

db.create_all()
