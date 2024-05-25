
from app.extensions import database

class Pengarang(database.Model):
	__tablename__ = 'Pengarang'

	Id = database.Column(database.Integer, primary_key=True, autoincrement=True)
	Nama = database.Column(database.String(32), nullable=False)
	Nasionalitas = database.Column(database.String(32))
	TanggalLahir = database.Column(database.Date)

	def __repr__(self):
		return f"<Pengarang {Pengarang.Id}>"
