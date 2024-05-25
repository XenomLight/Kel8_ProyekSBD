from app.extensions import database
from app.buku.database.rak.definisi import Rak


def tambah(LantaiNomor, Bagian, Kapasitas):
	new_rak = Rak(
		LantaiNomor=LantaiNomor,
		Bagian=Bagian,
		Kapasitas=Kapasitas
	)
	database.session.add(new_rak)
	database.session.commit()
	return new_rak


def hapus(Id):
	rak = Rak.query.get(Id)
	if not rak:
		return False

	database.session.delete(rak)
	database.session.commit()
	return True


def perbarui(Id, LantaiNomor=None, Bagian=None, Kapasitas=None):
	rak = Rak.query.get(Id)
	if not rak:
		return None

	if LantaiNomor is not None:
		rak.LantaiNomor = LantaiNomor
	if Bagian is not None:
		rak.Bagian = Bagian
	if Kapasitas is not None:
		rak.Kapasitas = Kapasitas
	database.session.commit()
	return rak
