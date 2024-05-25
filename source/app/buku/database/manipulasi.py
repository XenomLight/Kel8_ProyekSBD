# fungsi-fungsi untuk konversi data dari route untuk dicatata dalam database dengan benar

from app.buku.database.buku.definisi import Buku
from app.buku.database.buku import manipulasi as manipulasi_buku
from app.buku.database.dikategorikan import manipulasi as manipulasi_dikategorikan
from app.buku.database.kategori_buku import manipulasi as manipulasi_kategori_buku
from app.buku.database.penerbit import manipulasi as manipulasi_penerbit
from app.buku.database.pengarang import manipulasi as manipulasi_pengarang
from app.buku.database.rak import manipulasi as manipulasi_rak


def tambah_buku_dari_route(request_form):
	#manipulasi_kategori_buku.tambah()
	#manipulasi_penerbit.tambah()
	#manipulasi_pengarang.tambah()
	#manipulasi_rak.tambah()

	manipulasi_buku.tambah(
		request_form["Judul"],
		request_form["ISBN"],
		request_form["TahunPublikasi"],
		request_form.get("StatusTersedia") == '',
		None,
		None,
		None
	)

def hapus_buku_dari_route(Id, request_form):
	manipulasi_buku.hapus(Id)


def perbarui_buku_dari_route(Id, request_form):
	manipulasi_buku.perbarui(
		Id,
		request_form["Judul"],
		request_form["ISBN"],
		request_form["TahunPublikasi"],
		request_form["StatusTersedia"],
		request_form["Pengarang"],
		request_form["Penerbit"],
		request_form["Rak"]
	)
