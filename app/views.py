from flask import request, redirect, render_template
from . import app

@app.route("/")
def index():
	start_page = "/admin/"
	if request.environ.get("REMOTE_USER","") != "":
		return redirect(start_page)
	return render_template("start.html", start_page=start_page)

