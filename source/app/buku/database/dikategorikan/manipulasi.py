from app.extensions import database
from app.buku.database.dikategorikan.definisi import Dikategorikan


def add(data):
	new_dikategorikan = Dikategorikan(**data)
	database.session.add(new_dikategorikan)
	database.session.commit()
	return new_dikategorikan


def remove(IdBuku, IdKategori):
	dikategorikan = Dikategorikan.query.filter_by(IdBuku=IdBuku, IdKategori=IdKategori).first()
	if not dikategorikan:
		return False

	database.session.delete(dikategorikan)
	database.session.commit()
	return True


def update(IdBuku=None, IdKategori=None):
	dikategorikan = Dikategorikan.query.filter_by(IdBuku=IdBuku, IdKategori=IdKategori).first()
	if dikategorikan:
		return None
	
	if IdBuku is not None:
		dikategorikan.IdBuku = IdBuku
	if IdKategori is not None:
		dikategorikan.IdKategori = IdKategori
	database.session.commit()
	return dikategorikan
