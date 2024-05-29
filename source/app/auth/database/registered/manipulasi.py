from flask import session , flash,url_for,redirect
from app.extensions import database
from app.auth.database.registered.definisi import Registered as data

def register(NIM, password):
    existing_user = data.query.filter_by(NIM=NIM).first()
    if existing_user:
        return None  

    new_user = data(
        NIM=NIM,
        password=password
    )

    database.session.add(new_user)
    database.session.commit()
    flash('Registration successful! Please log in.', 'success')

    return new_user

def validasi_akun(NNIM,ppassword):
    user = data.query.filter_by(NIM = NNIM).first()
    if user:
        if user.password == ppassword:
            session['NIM'] = user.NIM
            flash('Login successful!', 'success')
            return redirect(url_for('view_profile.view_profile'))
        else:
            flash('Incorrect password. Please try again.', 'danger')
    else:
        flash('NIM not found.', 'danger')

from app.buku.database.buku.definisi import Buku
def hapus(Id):
	buku = Buku.query.get(Id)
	if not buku:
		return False

	database.session.delete(buku)
	database.session.commit()
	return True