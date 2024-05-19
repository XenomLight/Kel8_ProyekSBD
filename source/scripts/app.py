from flask import Flask
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

from .routes.home import home_blueprint
from .routes.view.buku import view_buku_blueprint
from .routes.view.mahasiswa import view_mahasiswa_blueprint
from .routes.view.pinjam import view_pinjam_blueprint

app = Flask(".")
app.register_blueprint(home_blueprint)
app.register_blueprint(view_buku_blueprint)
app.register_blueprint(view_mahasiswa_blueprint)
app.register_blueprint(view_pinjam_blueprint)


def main():
	app.run(debug=True)


if __name__ == "__main__":
	main()
