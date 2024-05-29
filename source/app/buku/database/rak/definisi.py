
from app.extensions import database

class Rak(database.Model):
	__tablename__ = 'Rak'

	Id = database.Column(database.Integer, primary_key=True, autoincrement=True)
	LantaiNomor = database.Column(database.String(1), nullable=False)
	Bagian = database.Column(database.String(2), nullable=False)
	Kapasitas = database.Column(database.Integer, nullable=False)

	def __repr__(self):
		return f"<Rak {{Rak.Id}}>"
