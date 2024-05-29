from flask import Blueprint, render_template, request, redirect

from app.buku.database import manipulasi as manipulasi_database_buku

NAMA_TEMPLATE_VIEW_SEMUA_BUKU: str = "view_buku.html"
NAMA_TEMPLATE_EDIT_BUKU: str = "edit_buku.html"
NAMA_TEMPLATE_TAMBAH_BUKU: str = "tambah_buku.html"
NAMA_TEMPLATE_PERBARUI_BUKU: str = "perbarui_buku.html"
NAMA_TEMPLATE_HAPUS_BUKU: str = "hapus_buku.html"

view_buku_blueprint = Blueprint("view_buku", __name__, template_folder="templates")


@view_buku_blueprint.route("/buku", methods=["GET"])
def view_buku():
	buku_view_semua = manipulasi_database_buku.select_semua_buku_dari_view_buku()
	return render_template(NAMA_TEMPLATE_VIEW_SEMUA_BUKU, buku_buku=buku_view_semua)


@view_buku_blueprint.route("/buku/tambah", methods=["POST", "GET"])
def tambah_buku():
	if request.method == "POST":
		manipulasi_database_buku.tambah_buku_dari_route(request.form)
		return redirect("/buku")

	return render_template(
		NAMA_TEMPLATE_EDIT_BUKU,
		action='Tambah',
		form_action='/buku/tambah',
		buku={},
		pengarang={},
		penerbit={},
		rak={},
		kategoriBuku={}
	)


@view_buku_blueprint.route("/buku/perbarui/<int:Id>", methods=["POST", "GET"])
def perbarui_buku(Id):
	if request.method == "POST":
		manipulasi_database_buku.perbarui_buku_dari_route(Id, request.form)
		return redirect("/buku")

	buku, kategoriBuku, penerbit, pengarang, rak = manipulasi_database_buku.get_buku_dengan_tabel_berrelasi(Id)
	return render_template(
		NAMA_TEMPLATE_EDIT_BUKU,
		action='Perbarui',
		form_action='/buku/perbarui/' + str(Id),
		buku=buku,
		pengarang=pengarang,
		penerbit=penerbit,
		rak=rak,
		kategoriBuku=kategoriBuku
	)


@view_buku_blueprint.route("/buku/hapus/<int:Id>", methods=["POST", "GET"])
def hapus_buku(Id):
	manipulasi_database_buku.hapus_buku_dari_route(Id)
	return redirect("/buku")

