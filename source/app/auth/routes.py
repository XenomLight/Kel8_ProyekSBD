from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import database as db
from ..extensions import User

NAMA_TEMPLATE_LOGIN: str = "login.html"
NAMA_TEMPLATE_REGISTER: str = "register.html"

auth_blueprint = Blueprint("login", __name__, template_folder="templates")
register_blueprint = Blueprint("register", __name__, template_folder="templates")

@auth_blueprint.route('/auth', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = user.username
            session['nim_nama_mhs'] = user.nim_nama_mhs
            return redirect(url_for('profile.profile'))
        else:
            return 'Invalid username or password. Please try again.'
    return render_template(NAMA_TEMPLATE_LOGIN)

@register_blueprint.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = user.username
            session['nim_nama_mhs'] = user.nim_nama_mhs
            return redirect(url_for('profile.profile'))
        else:
            return 'Invalid username or password. Please try again.'
    return render_template(NAMA_TEMPLATE_REGISTER)

@auth_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.home'))
