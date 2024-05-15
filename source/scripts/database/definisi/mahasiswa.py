
from ..database import database

class Mahasiswa(database.Model):
	__tablename__ = "Mahasiswa"

	NIM = database.Column(database.String(12), primary_key=True)
	NamaLengkap = database.Column(database.String(64), nullable=False)
	Email = database.Column(database.String(64))
	NomorTelepon = database.Column(database.String(15))

	def __repr__(self):
		return f"<Mahasiswa {Mahasiswa.NIM}>"
