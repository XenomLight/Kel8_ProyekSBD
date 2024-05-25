from flask import Blueprint, render_template, request, redirect

from app.buku.database.buku.definisi import Buku
from app.buku.database import manipulasi as manipulasi_database_buku

NAMA_TEMPLATE_VIEW_BUKU: str = "view_buku.html"
NAMA_TEMPLATE_TAMBAH_BUKU: str = "tambah_buku.html"
NAMA_TEMPLATE_PERBARUI_BUKU: str = "perbarui_buku.html"
NAMA_TEMPLATE_HAPUS_BUKU: str = "hapus_buku.html"

view_buku_blueprint = Blueprint("view_buku", __name__, template_folder="templates")

@view_buku_blueprint.route("/buku", methods=["GET"])
def view_buku():
	buku_buku = Buku.query.order_by(Buku.Judul).all()
	return render_template(NAMA_TEMPLATE_VIEW_BUKU, buku_buku=buku_buku)


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

	buku = Buku.query.get(Id)
	return render_template(NAMA_TEMPLATE_PERBARUI_BUKU)


@view_buku_blueprint.route("/buku/hapus/<int:Id>", methods=["POST", "GET"])
def hapus_buku(Id):
	#if request.method == "POST":
	#	manipulasi_database_buku.hapus_buku_dari_route(request.form)
	#	return redirect("/buku")
	#
	#return render_template(NAMA_TEMPLATE_HAPUS_BUKU)

	manipulasi_database_buku.hapus_buku_dari_route(Id, request.form)
	return redirect("/buku")

