from flask import render_template

from app.home import blueprint

NAMA_TEMPLATE_HOME: str = '/home.html'

@blueprint.route("/")
def index():
	return render_template(NAMA_TEMPLATE_HOME)
