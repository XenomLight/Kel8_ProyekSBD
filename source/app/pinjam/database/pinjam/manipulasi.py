from app.extensions import database
from app.pinjam.database.pinjam.definisi import Pinjam
from sqlalchemy import text
from datetime import datetime


def add(request_form):
    Id = request_form["Id"]
    IdBuku = request_form["IdBuku"]
    NIM = request_form["NIM"]
    TanggalPeminjaman = datetime.strptime(request_form["TanggalPeminjaman"], '%Y-%m-%d').date()
    TanggalPengembalian = datetime.strptime(request_form["TanggalPengembalian"], '%Y-%m-%d').date()
    Status = request_form["Status"]
    new_pinjam = Pinjam(
        Id=Id,
        IdBuku=IdBuku,
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


def update(Id, IdBuku,NIM=None, TanggalPeminjaman=None, TanggalPengembalian=None, Status=None):
	pinjam = Pinjam.query.get(Id)
	if not pinjam:
		return None

	if Id is not None:
		pinjam.Id = Id
	if IdBuku is not none:
		pinjam.IdBuku = IdBuku
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

def view_semua_pinjam():
	return database.session.execute(text("""
SELECT *FROM Pinjam
""")).mappings().all()