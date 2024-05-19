from flask import Blueprint, render_template

NAMA_TEMPLATE_VIEW_PINJAMAN: str = "view/pinjam/index.html"

view_pinjam_blueprint = Blueprint("view_pinjam", ".")

@view_pinjam_blueprint.route("/pinjaman")
def view_pinjaman():
	return render_template(NAMA_TEMPLATE_VIEW_PINJAMAN)


@view_pinjam_blueprint.route("/pinjaman/tambah", methods=["POST", "GET"])
def tambah_pinjaman():
	return redirect("/pinjaman")


@view_pinjam_blueprint.route("/pinjaman/perbarui/<int:Id>", methods=["POST", "GET"])
def perbarui_pinjaman(Id):
	return redirect("/pinjaman")


@view_pinjam_blueprint.route("/pinjaman/hapus/<int:Id>", methods=["POST", "GET"])
def hapus_pinjaman(Id):
	return redirect("/pinjaman")
