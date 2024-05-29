from app.extensions import database
from app.buku.database.kategori_buku.definisi import KategoriBuku


def tambah(Jenis):
	new_kategori_buku = KategoriBuku(
		Jenis=Jenis
	)
	database.session.add(new_kategori_buku)
	database.session.commit()
	return new_kategori_buku


def hapus(Id):
	kategori_buku = KategoriBuku.query.get(Id)
	if not kategori_buku:
		return False

	database.session.delete(kategori_buku)
	database.session.commit()
	return True


def perbarui(Id, Jenis=None):
	kategori_buku = KategoriBuku.query.get(Id)
	if not kategori_buku:
		return None

	if Jenis is not None:
		kategori_buku.Jenis = Jenis
	database.session.commit()
	return kategori_buku