
from app.extensions import database

class Dikategorikan(database.Model):
	__tablename__ = 'Dikategorikan'

	IdBuku = database.Column(database.Integer, database.ForeignKey('Buku.Id'), primary_key=True, nullable=False)
	IdKategori = database.Column(database.Integer, database.ForeignKey('KategoriBuku.Id'), primary_key=True, nullable=False)

	def __repr__(self):
		return f"<Dikategorikan [IdBuku={Dikategorikan.IdBuku}, IdKategori={Dikategorikan.IdKategori}]>"
