from flask import Blueprint, render_template, request, redirect, url_for, session, request,flash
from app.auth.database.registered.definisi import Registered as data
from app.auth.database import manipulasi as edit_sql
from app.extensions import database as db

NAMA_TEMPLATE_LOGIN: str = "login.html"
NAMA_TEMPLATE_REGISTER: str = "register.html"

auth_blueprint = Blueprint("login", __name__, template_folder="templates")
register_blueprint = Blueprint("register", __name__, template_folder="templates")

@auth_blueprint.before_request
def check_session():
    if 'NIM' not in session and request.endpoint != 'login.login' and request.endpoint != 'login.register':
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login.login'))
    elif 'NIM' in session and request.endpoint == 'login.login':
        return redirect(url_for('profile'))
    
@auth_blueprint.route('/auth', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        edit_sql.login_route(request.form)
    return render_template(NAMA_TEMPLATE_LOGIN)

@register_blueprint.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        edit_sql.register_route(request.form)
        return redirect(url_for('login.login'))

    return render_template(NAMA_TEMPLATE_REGISTER)

@auth_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))
