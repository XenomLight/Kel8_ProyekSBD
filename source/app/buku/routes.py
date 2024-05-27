from flask import Blueprint, render_template, request, redirect

from app.buku.database.buku.definisi import Buku
from app.buku.database.dikategorikan.definisi import Dikategorikan
from app.buku.database.kategori_buku.definisi import KategoriBuku
from app.buku.database.penerbit.definisi import Penerbit
from app.buku.database.pengarang.definisi import Pengarang
from app.buku.database.rak.definisi import Rak

from app.buku.database import manipulasi as manipulasi_database_buku

NAMA_TEMPLATE_VIEW_SEMUA_BUKU: str = "view_semua_buku.html"
NAMA_TEMPLATE_VIEW_SATU_BUKU: str = "view_satu_buku.html"
NAMA_TEMPLATE_TAMBAH_BUKU: str = "tambah_buku.html"
NAMA_TEMPLATE_PERBARUI_BUKU: str = "perbarui_buku.html"
NAMA_TEMPLATE_HAPUS_BUKU: str = "hapus_buku.html"

view_buku_blueprint = Blueprint("view_buku", __name__, template_folder="templates")


@view_buku_blueprint.route("/buku", methods=["GET"])
def view_buku_semua():
	buku_view_semua = manipulasi_database_buku.select_semua_buku_dari_view_buku()
	return render_template(NAMA_TEMPLATE_VIEW_SEMUA_BUKU, buku_buku=buku_view_semua)


@view_buku_blueprint.route("/buku/<int:Id>", methods=["GET"])
def view_buku_satu(Id):
	buku_view_satu = manipulasi_database_buku.select_satu_buku_dari_view_buku(Id)
	return render_template(NAMA_TEMPLATE_VIEW_SATU_BUKU, buku=buku_view_satu)


@view_buku_blueprint.route("/buku/tambah", methods=["POST", "GET"])
def tambah_buku():
	if request.method == "POST":
		manipulasi_database_buku.tambah_buku_dari_route(request.form)
		return redirect("/buku")

	return render_template(NAMA_TEMPLATE_TAMBAH_BUKU)


@view_buku_blueprint.route("/buku/perbarui/<int:Id>", methods=["POST", "GET"])
def perbarui_buku(Id):
	if request.method == "POST":
		manipulasi_database_buku.perbarui_buku_dari_route(Id, request.form)
		return redirect("/buku")

	buku = manipulasi_database_buku.select_satu_buku_dari_view_buku(Id)
	return render_template(NAMA_TEMPLATE_PERBARUI_BUKU)


@view_buku_blueprint.route("/buku/hapus/<int:Id>", methods=["POST", "GET"])
def hapus_buku(Id):
	manipulasi_database_buku.hapus_buku_dari_route(Id, request.form)
	return redirect("/buku")

