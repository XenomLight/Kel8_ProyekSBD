from flask_sqlalchemy import SQLAlchemy


database = SQLAlchemy()

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), unique=True, nullable=False)
    password = database.Column(database.String(100), nullable=False)
    nim_nama_mhs = database.Column(database.String(100), nullable=False)