from flask import Blueprint, render_template,redirect,request
from app.pinjam.database.pinjam.definisi import Pinjam
from app.pinjam.database.pinjam import manipulasi
NAMA_TEMPLATE_VIEW_PINJAMAN: str = "view_pinjam.html"
NAMA_TEMPLATE_EDIT_PINJAM: str = "edit_pinjam.html"
view_pinjam_blueprint = Blueprint("view_pinjam", __name__, template_folder="templates")

@view_pinjam_blueprint.route("/pinjaman")
def view_pinjaman():
    selector = manipulasi.view_semua_pinjam()
    return render_template(NAMA_TEMPLATE_VIEW_PINJAMAN,sl = selector)


@view_pinjam_blueprint.route("/pinjaman/tambah", methods=["POST", "GET"])
def tambah_pinjaman():
	if request.method == "POST":
		manipulasi.add(request.form)
		return redirect("/pinjaman")
	return render_template(
		NAMA_TEMPLATE_EDIT_PINJAM,
		action='Tambah',
		form_action='/pinjaman/tambah',
		Pinjam={}
	)


@view_pinjam_blueprint.route("/pinjaman/perbarui/<int:Id>", methods=["POST", "GET"])
def perbarui_pinjaman(Id):
    pinjam = Pinjam.query.get(Id)
    if request.method == "POST":
        manipulasi.update(request.form["Id"],request.form["IdBuku"],request.form["NIM"],request.form["TanggalPeminjaman"],request.form["TanggalPengembalian"],request.form["Status"])
        return redirect("/pinjaman")
    
    return render_template(
        NAMA_TEMPLATE_EDIT_PINJAM,
        action='Perbarui',
        form_action='/pinjaman/perbarui/' + str(Id),
        Pinjam=pinjam
    )

@view_pinjam_blueprint.route("/pinjaman/hapus/<int:Id>", methods=["POST", "GET"])
def hapus_pinjaman(Id):
    manipulasi.remove(Id)
    return redirect("/pinjaman")
