
from ..database import database

class Penerbit(database.Model):
	__tablename__ = 'Penerbit'

	Id = database.Column(database.Integer, primary_key=True, autoincrement=True)
	Nama = database.Column(database.String(32), nullable=False)
	LokasiMarkas = database.Column(database.String(32))
	TahunPendirian = database.Column(database.Integer)

	def __repr__(self):
		return f"<Penerbit {Penerbit.Id}>"
