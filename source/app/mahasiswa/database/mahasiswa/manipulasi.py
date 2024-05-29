from app.extensions import database
from app.mahasiswa.database.mahasiswa.definisi import Mahasiswa
from sqlalchemy import text


def add(request_form):
    NIM = request_form["NIM"]
    NamaLengkap = request_form["NamaLengkap"]
    Email = request_form["Email"]
    NomorTelepon = request_form["NomorTelepon"]
    new_mahasiswa = Mahasiswa(
		NIM=NIM,
		NamaLengkap=NamaLengkap,
		Email=Email,
		NomorTelepon=NomorTelepon
	)
    database.session.add(new_mahasiswa)
    database.session.commit()
    return new_mahasiswa


def remove(NIM):
	mahasiswa = Mahasiswa.query.get(NIM)
	if not mahasiswa:
		return False

	database.session.delete(mahasiswa)
	database.session.commit()
	return True


def update(NIM, NamaLengkap=None, Email=None, NomorTelepon=None):
	mahasiswa = Mahasiswa.query.get(NIM)
	if not mahasiswa:
		return None

	if NamaLengkap is not None:
		mahasiswa.NamaLengkap = NamaLengkap
	if Email is not None:
		mahasiswa.Email = Email
	if NomorTelepon is not None:
		mahasiswa.NomorTelepon = NomorTelepon
	database.session.commit()
	return mahasiswa

def view_semua_mahasiswa():
	return database.session.execute(text("""
SELECT *FROM mahasiswa
""")).mappings().all()
 
 