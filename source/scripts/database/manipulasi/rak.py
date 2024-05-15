from ..database import database
from ..definisi.rak import Rak


def add(LantaiNomor, Bagian, Kapasitas):
	new_rak = Rak(
		LantaiNomor=LantaiNomor,
		Bagian=Bagian,
		Kapasitas=Kapasitas
	)
	database.session.add(new_rak)
	database.session.commit()
	return new_rak


def remove(Id):
	rak = Rak.query.get(Id)
	if not rak:
		return False

	database.session.delete(rak)
	database.session.commit()
	return True


def update(Id, LantaiNomor=None, Bagian=None, Kapasitas=None):
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
