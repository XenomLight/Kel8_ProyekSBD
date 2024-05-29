from flask import Blueprint, render_template, request, session, redirect, url_for,flash

from app.mahasiswa.database.mahasiswa.definisi import Mahasiswa
from app.mahasiswa.database.mahasiswa import manipulasi as manipulasi_database_mahasiswa

NAMA_TEMPLATE_VIEW_PROFILE: str = "view_profile.html"

view_profile_blueprint = Blueprint("view_profile", __name__, template_folder="templates")

@view_profile_blueprint.before_request
def check_session():
    if 'NIM' not in session and request.endpoint != 'login.login' and request.endpoint != 'login.register':
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login.login'))

    
@view_profile_blueprint.route("/profile")
def view_profile():
    if 'NIM' in session:
        user = Mahasiswa.query.filter_by(NIM=session['NIM']).first()
    return render_template(NAMA_TEMPLATE_VIEW_PROFILE, user=user)





