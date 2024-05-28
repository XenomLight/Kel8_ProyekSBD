from flask import Blueprint, render_template, request, session, redirect, url_for

from app.mahasiswa.database.mahasiswa.definisi import Mahasiswa
from app.mahasiswa.database.mahasiswa import manipulasi as manipulasi_database_mahasiswa

NAMA_TEMPLATE_VIEW_PROFILE: str = "view_profile.html"

view_profile_blueprint = Blueprint("view_profile", __name__, template_folder="templates")

@view_profile_blueprint.route("/profile")
def view_profile():
    if 'logged_in' in session:
        return render_template('/profile', nim=session['nim'])
    else:
        return redirect(url_for('auth.login'))




