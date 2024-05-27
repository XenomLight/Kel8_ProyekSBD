from flask import Flask



from configuration import Configuration
from app.extensions import database


def create_app(configuration = Configuration):
	app = Flask(__name__)
	app.config.from_object(configuration)

	database.init_app(app)

	from app.home import blueprint as home_blueprint
	from .auth.routes import auth_blueprint
	from .buku.routes import view_buku_blueprint
	from .mahasiswa.routes import view_mahasiswa_blueprint
	from .pinjam.routes import view_pinjam_blueprint
	from .profile.routes import view_profile_blueprint
	app.register_blueprint(home_blueprint)
	app.register_blueprint(auth_blueprint)
	app.register_blueprint(view_buku_blueprint)
	app.register_blueprint(view_mahasiswa_blueprint)
	app.register_blueprint(view_pinjam_blueprint)
	app.register_blueprint(view_profile_blueprint)


	return app


def main():
	create_app().run(debug=True)


if __name__ == "__main__":
	main()
