from ..database import database
from ..definisi.penerbit import Penerbit


def add(Nama, LokasiMarkas, TahunPendirian):
	new_penerbit = Penerbit(
		Nama=Nama,
		LokasiMarkas=LokasiMarkas,
		TahunPendirian=TahunPendirian
	)
	database.session.add(new_penerbit)
	database.session.commit()
	return new_penerbit


def remove(Id):
	penerbit = Penerbit.query.get(Id)
	if not penerbit:
		return False

	database.session.delete(penerbit)
	database.session.commit()
	return True


def update(Id, Nama=None, LokasiMarkas=None, TahunPendirian=None):
	penerbit = Penerbit.query.get(Id)
	if not penerbit:
		return None

	if Nama is not None:
		penerbit.Nama = Nama
	if LokasiMarkas is not None:
		penerbit.LokasiMarkas = LokasiMarkas
	if TahunPendirian is not None:
		penerbit.TahunPendirian = TahunPendirian
	database.session.commit()
	return penerbit