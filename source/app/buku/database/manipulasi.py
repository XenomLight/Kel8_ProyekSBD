# fungsi-fungsi untuk konversi data dari route untuk dicatat dalam database dengan benar

from datetime import datetime
from sqlalchemy import text

from app.extensions import database

from app.buku.database.buku.definisi import Buku
from app.buku.database.kategori_buku.definisi import KategoriBuku
from app.buku.database.penerbit.definisi import Penerbit
from app.buku.database.pengarang.definisi import Pengarang
from app.buku.database.rak.definisi import Rak
from app.buku.database.buku import manipulasi as manipulasi_buku
from app.buku.database.kategori_buku import manipulasi as manipulasi_kategori_buku
from app.buku.database.penerbit import manipulasi as manipulasi_penerbit
from app.buku.database.pengarang import manipulasi as manipulasi_pengarang
from app.buku.database.rak import manipulasi as manipulasi_rak

def get_buku_dengan_tabel_berrelasi(Id):
	buku = Buku.query.get(Id)
	if not buku:
		return None

	rak = Rak.query.get(buku.IdRak)
	penerbit = Penerbit.query.get(buku.IdPenerbit)
	pengarang = Pengarang.query.get(buku.IdPengarang)
	kategori_buku = KategoriBuku.query.get(buku.IdKategoriBuku)

	return buku, kategori_buku, penerbit, pengarang, rak


def get_penerbit_dari_non_key(Nama, LokasiMarkas, TahunPendirian):
	return Penerbit.query.filter_by(
		Nama=Nama,
		LokasiMarkas=LokasiMarkas,
		TahunPendirian=TahunPendirian).first()


def get_pengarang_dari_non_key(Nama, Nasionalitas, TanggalLahir):
	return Pengarang.query.filter_by(
		Nama=Nama,
		Nasionalitas=Nasionalitas,
		TanggalLahir=TanggalLahir
	).first()


def get_kategori_buku_dari_non_key(Jenis):
	return KategoriBuku.query.filter_by(Jenis=Jenis).first()


def tambah_buku_dari_route(request_form):
	print(request_form)

	kategori_buku = get_kategori_buku_dari_non_key(request_form["KategoriBukuJenis"])

	penerbit = get_penerbit_dari_non_key(
		request_form["PenerbitNama"],
		request_form["PenerbitLokasiMarkas"],
		request_form["PenerbitTahunPendirian"]
	)

	pengarang_tanggal_lahir = datetime.strptime(request_form["PengarangTanggalLahir"], '%Y-%m-%d')
	pengarang = get_penerbit_dari_non_key(
		request_form["PengarangNama"],
		request_form["PengarangNasionalitas"], 
		pengarang_tanggal_lahir
	)

	rak = Rak.query.get(request_form["RakId"])

	if not kategori_buku:
		kategori_buku = manipulasi_kategori_buku.tambah(
			request_form["KategoriBukuJenis"]
		)

	if not penerbit:
		penerbit = manipulasi_penerbit.tambah(
			request_form["PenerbitNama"],
			request_form["PenerbitLokasiMarkas"],
			request_form["PenerbitTahunPendirian"]
		)

	if not pengarang:
		pengarang = manipulasi_pengarang.tambah(
			request_form["PengarangNama"],
			request_form["PengarangNasionalitas"],
			pengarang_tanggal_lahir
		)

	if not rak:
		rak = manipulasi_rak.tambah(
			request_form["RakId"],
			request_form["RakLantaiNomor"],
			request_form["RakBagian"],
			request_form["RakKapasitas"]
		)

	manipulasi_buku.tambah(
		request_form["Judul"],
		request_form["ISBN"],
		request_form["TahunPublikasi"],
		request_form.get("StatusTersedia") == '',
		kategori_buku.Id,
		pengarang.Id,
		penerbit.Id,
		rak.Id
	)


def hapus_elemen_orphan_tabel_buku(kategori_buku, pengarang, penerbit, rak):
	if Buku.query.filter_by(IdKategoriBuku=kategori_buku.Id).count() <= 0:
		manipulasi_kategori_buku.hapus(kategori_buku.Id)
	if Buku.query.filter_by(IdPengarang=pengarang.Id).count() <= 0:
		manipulasi_pengarang.hapus(pengarang.Id)
	if Buku.query.filter_by(IdPenerbit=penerbit.Id).count() <= 0:
		manipulasi_penerbit.hapus(penerbit.Id)
	if Buku.query.filter_by(IdRak=rak.Id).count() <= 0:
		manipulasi_rak.hapus(rak.Id)


def hapus_buku_dari_route(Id):
	buku, kategori_buku, penerbit, pengarang, rak = get_buku_dengan_tabel_berrelasi(Id)
	manipulasi_buku.hapus(buku.Id)
	hapus_elemen_orphan_tabel_buku(kategori_buku, pengarang, penerbit, rak)


def perbarui_buku_dari_route(Id, request_form):
	_, old_kategori_buku, old_penerbit, old_pengarang, old_rak, = get_buku_dengan_tabel_berrelasi(Id)

	new_kategori_buku = KategoriBuku.query.filter_by(Jenis=request_form["KategoriBukuJenis"]).first()
	new_penerbit = Penerbit.query.filter_by(Nama=request_form["PenerbitNama"]).first()
	new_pengarang_tanggal_lahir = datetime.strptime(request_form["PengarangTanggalLahir"], '%Y-%m-%d')
	new_pengarang = Penerbit.query.filter_by(Nama=request_form["PengarangNama"]).first()
	new_rak = Rak.query.get(request_form["RakId"])

	if not new_kategori_buku:
		new_kategori_buku = manipulasi_kategori_buku.tambah(
			request_form["KategoriBukuJenis"]
		)
	else:
		manipulasi_kategori_buku.perbarui(
			new_kategori_buku.Id,
			request_form["KategoriBukuJenis"]
		)

	if not new_pengarang:
		new_pengarang = manipulasi_pengarang.tambah(
			request_form["PengarangNama"],
			request_form["PengarangNasionalitas"],
			new_pengarang_tanggal_lahir
		)
	else:
		manipulasi_pengarang.perbarui(
			new_pengarang.Id,
			request_form["PengarangNama"],
			request_form["PengarangNasionalitas"],
			new_pengarang_tanggal_lahir
		)

	if not new_penerbit:
		new_penerbit = manipulasi_penerbit.tambah(
			request_form["PenerbitNama"],
			request_form["PenerbitLokasiMarkas"],
			request_form["PenerbitTahunPendirian"]
		)
	else:
		manipulasi_penerbit.perbarui(
			new_penerbit.Id,
			request_form["PenerbitNama"],
			request_form["PenerbitLokasiMarkas"],
			request_form["PenerbitTahunPendirian"]
		)

	if not new_rak:
		new_rak = manipulasi_rak.tambah(
			request_form["RakId"],
			request_form["RakLantaiNomor"],
			request_form["RakBagian"],
			request_form["RakKapasitas"]
		)
	else:
		manipulasi_rak.perbarui(
			new_penerbit.Id,
			request_form["RakLantaiNomor"],
			request_form["RakBagian"],
			request_form["RakKapasitas"]
		)

	manipulasi_buku.perbarui(
		Id=Id,
		Judul=request_form["Judul"],
		ISBN=request_form["ISBN"],
		TahunPublikasi=request_form["TahunPublikasi"],
		StatusTersedia=request_form.get("StatusTersedia") == '',
		IdKategoriBuku=new_kategori_buku.Id,
		IdPengarang=new_pengarang.Id,
		IdPenerbit=new_penerbit.Id,
		IdRak=new_rak.Id
	)

	hapus_elemen_orphan_tabel_buku(old_kategori_buku, old_pengarang, old_penerbit, old_rak)


def select_semua_buku_dari_view_buku():
	return database.session.execute(text("""
SELECT 
b.Id, b.Judul, b.ISBN, b.TahunPublikasi, b.StatusTersedia,
pg.Nama AS NamaPengarang,
pe.Nama AS NamaPenerbit,
b.IdRak AS IdRak
FROM
Buku b
LEFT JOIN Pengarang pg ON b.IdPengarang = pg.Id
LEFT JOIN Penerbit pe ON b.IdPenerbit = pe.Id
""")).mappings().all()
