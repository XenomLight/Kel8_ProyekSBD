from app.extensions import database
from app.buku.database.buku.definisi import Buku


def tambah(Judul, ISBN, TahunPublikasi, StatusTersedia, IdKategoriBuku, IdPengarang, IdPenerbit, IdRak):
	new_buku = Buku(
		Judul=Judul,
		ISBN=ISBN,
		TahunPublikasi=TahunPublikasi,
		StatusTersedia=StatusTersedia,
		IdPengarang=IdPengarang,
		IdPenerbit=IdPenerbit,
		IdRak=IdRak,
		IdKategoriBuku=IdKategoriBuku
	)
	database.session.add(new_buku)
	database.session.commit()
	return new_buku


def hapus(Id):
	buku = Buku.query.get(Id)
	if not buku:
		return False

	database.session.delete(buku)
	database.session.commit()
	return True


def perbarui(Id, Judul=None, ISBN=None, TahunPublikasi=None, StatusTersedia=None, IdKategoriBuku=None, IdPenerbit=None, IdPengarang=None, IdRak=None):
	buku = Buku.query.get(Id)
	if not buku:
		return None

	if Judul is not None:
		buku.Judul = Judul
	if ISBN is not None:
		buku.ISBN = ISBN
	if TahunPublikasi is not None:
		buku.TahunPublikasi = TahunPublikasi
	if StatusTersedia is not None:
		buku.StatusTersedia = StatusTersedia
	if IdKategoriBuku is not None:
		buku.IdKategoriBuku = IdKategoriBuku
	if IdPenerbit is not None:
		buku.IdPenerbit = IdPenerbit
	if IdPengarang is not None:
		buku.IdPengarang = IdPengarang
	if IdRak is not None:
		buku.IdRak = IdRak

	database.session.commit()
	return buku
	
