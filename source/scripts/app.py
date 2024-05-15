from flask import Flask
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(".")


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/buku")
def view_buku():
	return redirect("/")


@app.route("/mahasiswa")
def view_mahasiswa():
	return redirect("/")


@app.route("/pinjaman")
def view_pinjaman():
	return redirect("/")


@app.route("/buku/tambah")
def tambah_buku():
	return redirect("/")


@app.route("/buku/perbarui")
def perbarui_buku():
	return redirect("/")


@app.route("/buku/hapus")
def hapus_buku():
	return redirect("/")


@app.route("/mahasiswa/tambah")
def tambah_mahasiswa():
	return redirect("/")


@app.route("/mahasiswa/perbarui")
def perbarui_mahasiswa():
	return redirect("/")


@app.route("/mahasiswa/hapus")
def hapus_mahasiswa():
	return redirect("/")


@app.route("/pinjaman/tambah")
def tambah_pinjaman():
	return redirect("/")


@app.route("/pinjaman/perbarui")
def perbarui_pinjaman():
	return redirect("/")


@app.route("/pinjaman/hapus")
def hapus_pinjaman():
	return redirect("/")


def main():
	app.run(debug=True)


if __name__ == "__main__":
	main()
