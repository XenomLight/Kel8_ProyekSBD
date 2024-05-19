from flask import Blueprint, render_template

NAMA_TEMPLATE_VIEW_MAHASISWA: str = "view/mahasiswa/index.html"

view_mahasiswa_blueprint = Blueprint("view_mahasiswa", ".")

@view_mahasiswa_blueprint.route("/mahasiswa")
def view_mahasiswa():
	return render_template(NAMA_TEMPLATE_VIEW_MAHASISWA)


@view_mahasiswa_blueprint.route("/mahasiswa/tambah", methods=["POST", "GET"])
def tambah_mahasiswa():
	return redirect("/mahasiswa")


@view_mahasiswa_blueprint.route("/mahasiswa/perbarui/<int:Id>", methods=["POST", "GET"])
def perbarui_mahasiswa(Id):
	return redirect("/mahasiswa")


@view_mahasiswa_blueprint.route("/mahasiswa/hapus/<int:Id>", methods=["POST", "GET"])
def hapus_mahasiswa(Id):
	return redirect("/mahasiswa")
