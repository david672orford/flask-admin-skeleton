from flask_admin import Admin
from flask_admin.contrib.sqla.view import ModelView as InsecureModelView
from flask_admin.form import SecureForm
from . import app
from .models import db, Users

admin = Admin(app, name=app.config['APP_DISPLAY_NAME'])

# Create base model view
class ModelView(InsecureModelView):
    form_base_class = SecureForm
    action_disallowed_list = ['delete']     # no mass delete
    page_size = 15

# Base model view with support for the HTML editor field
class HtmlModelView(ModelView):
    load_html_editor = True

class UsersView(ModelView):
	pass

admin.add_view(UsersView(Users, db.session))

