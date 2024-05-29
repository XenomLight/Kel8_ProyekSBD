from flask import render_template,flash,session,redirect,url_for
from app.mahasiswa.database.mahasiswa.definisi import Mahasiswa as data
from app.home import blueprint

NAMA_TEMPLATE_HOME: str = '/home.html'

@blueprint.route("/")
def index():
    user = None 
    if "NIM" in session:
        user = data.query.filter_by(NIM=session['NIM']).first()
    return render_template('home.html', user=user)
