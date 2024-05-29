
from app.extensions import database

class Buku(database.Model):
	__tablename__ = 'Buku'

	Id = database.Column(database.Integer, primary_key=True, autoincrement=True)
	Judul = database.Column(database.String(15), nullable=False)
	ISBN = database.Column(database.String(13), nullable=False)
	TahunPublikasi = database.Column(database.Integer)
	StatusTersedia = database.Column(database.Boolean)
	IdPengarang = database.Column(database.Integer, database.ForeignKey('Pengarang.Id'))
	IdPenerbit = database.Column(database.Integer, database.ForeignKey('Penerbit.Id'))
	IdRak = database.Column(database.Integer, database.ForeignKey('Rak.Id'))#, nullable=False)
	IdKategoriBuku = database.Column(database.Integer, database.ForeignKey('KategoriBuku.Id'))

	def __repr__(self):
		return f"<Buku {self.Id}>"
