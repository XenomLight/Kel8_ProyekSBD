from flask import Blueprint, render_template

NAMA_TEMPLATE_HOME: str = "index.html"

home_blueprint = Blueprint("home", ".")

@home_blueprint.route("/")
def index():
	return render_template(NAMA_TEMPLATE_HOME)
