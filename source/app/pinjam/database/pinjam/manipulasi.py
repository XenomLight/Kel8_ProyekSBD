from ..database import database
from ..definisi.pinjam import Pinjam


def add(Id, NIM, TanggalPeminjaman, TanggalPengembalian=None, Status=None):
	new_pinjam = Pinjam(
		Id=Id,
		NIM=NIM,
		TanggalPeminjaman=TanggalPeminjaman,
		TanggalPengembalian=TanggalPengembalian,
		Status=Status
	)
	database.session.add(new_pinjam)
	database.session.commit()
	return new_pinjam


def remove(Id):
	pinjam = Pinjam.query.get(Id)
	if not pinjam:
		return False

	database.session.delete(pinjam)
	database.session.commit()
	return True


def update(Id, NIM=None, TanggalPeminjaman=None, TanggalPengembalian=None, Status=None):
	pinjam = Pinjam.query.get(Id)
	if not pinjam:
		return None

	if Id is not None:
		pinjam.Id = Id
	if NIM is not None:
		pinjam.NIM = NIM
	if TanggalPeminjaman is not None:
		pinjam.TanggalPeminjaman = TanggalPeminjaman
	if TanggalPengembalian is not None:
		pinjam.TanggalPengembalian = TanggalPengembalian
	if Status is not None:
		pinjam.Status = Status
	database.session.commit()
	return pinjam
