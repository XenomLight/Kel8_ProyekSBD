from flask import Blueprint, render_template

NAMA_TEMPLATE_VIEW_BUKU: str = "view/buku/index.html"

view_buku_blueprint = Blueprint("view_buku", ".")

@view_buku_blueprint.route("/buku")
def view_buku():
	return render_template(NAMA_TEMPLATE_VIEW_BUKU)


@view_buku_blueprint.route("/buku/tambah", methods=["POST", "GET"])
def tambah_buku():
	return redirect("/buku")


@view_buku_blueprint.route("/buku/perbarui/<int:Id>", methods=["POST", "GET"])
def perbarui_buku(Id):
	return redirect("/buku")


@view_buku_blueprint.route("/buku/hapus/<int:Id>", methods=["POST", "GET"])
def hapus_buku(Id):
	return redirect("/buku")
