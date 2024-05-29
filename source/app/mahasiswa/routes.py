from flask import Blueprint, render_template,redirect,request
from app.mahasiswa.database.mahasiswa import manipulasi as manipulasi
from app.mahasiswa.database.mahasiswa.definisi import Mahasiswa
NAMA_TEMPLATE_VIEW_MAHASISWA: str = "view_mahasiswa.html"
NAMA_TEMPLATE_TAMBAH_MAHASISWA: str = "edit_mahasiswa.html"

view_mahasiswa_blueprint = Blueprint("view_mahasiswa", __name__, template_folder="templates")

@view_mahasiswa_blueprint.route("/mahasiswa")
def view_mahasiswa():
    selector = manipulasi.view_semua_mahasiswa()
    return render_template(NAMA_TEMPLATE_VIEW_MAHASISWA,cek_jml_mhs=selector)


@view_mahasiswa_blueprint.route("/mahasiswa/tambah", methods=["POST", "GET"])
def tambah_mahasiswa():
	if request.method == "POST":
		manipulasi.add(request.form)
		return redirect("/mahasiswa")
	return render_template(
		NAMA_TEMPLATE_TAMBAH_MAHASISWA,
		action='Tambah',
		form_action='/mahasiswa/tambah',
		Mahasiswa={}
	)

@view_mahasiswa_blueprint.route("/mahasiswa/perbarui/<int:Id>", methods=["POST", "GET"])
def update(Id):
    mahasiswa = Mahasiswa.query.get(Id)
    if mahasiswa is None:
        return "Mahasiswa not found", 404

    if request.method == "POST":
        manipulasi.update(Id, request.form)
        return redirect("/mahasiswa")
    
    return render_template(
        NAMA_TEMPLATE_TAMBAH_MAHASISWA,
        action='Perbarui',
        form_action='/mahasiswa/perbarui/' + str(Id),
        mahasiswa=mahasiswa
    )
@view_mahasiswa_blueprint.route("/mahasiswa/hapus/<int:Id>", methods=["POST", "GET"])
def hapus_mahasiswa(Id):
    manipulasi.remove(Id)
    return redirect("/mahasiswa")
