from ..database import database
from ..definisi.pengarang import Pengarang


def add(Nama, Nasionalitas, TanggalLahir):
	new_pengarang = Pengarang(
		Nama=Nama,
		Nasionalitas=Nasionalitas,
		TanggalLahir=TanggalLahir
	)
	database.session.add(new_pengarang)
	database.session.commit()
	return new_pengarang


def remove(Id):
	pengarang = Pengarang.query.get(Id)
	if not pengarang:
		return False

	database.session.delete(pengarang)
	database.session.commit()
	return True


def update(Id, Nama=None, Nasionalitas=None, TanggalLahir=None):
	pengarang = Pengarang.query.get(Id)
	if not pengarang:
		return None

	if Nama is not None:
		pengarang.Nama = Nama
	if Nasionalitas is not None:
		pengarang.Nasionalitas = Nasionalitas
	if TanggalLahir is not None:
		pengarang.TanggalLahir = TanggalLahir
	database.session.commit()
	return pengarang
