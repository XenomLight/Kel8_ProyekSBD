
# tempat setor referensi database

from flask_sqlalchemy import SQLAlchemy
from ..app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
database = SQLAlchemy(app)


def main():
	pass


if __name__ == "__main__":
	main()
