from flask import Blueprint

blueprint = Blueprint('home', __name__, template_folder="templates")

from app.home import routes
