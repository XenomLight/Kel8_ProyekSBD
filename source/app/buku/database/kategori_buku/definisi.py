
from app.extensions import database

class KategoriBuku(database.Model):
	__tablename__ = 'KategoriBuku'

	Id = database.Column(database.Integer, primary_key=True, autoincrement=True)
	Jenis = database.Column(database.String(15), nullable=False)

	def __repr__(self):
		return f"<KategoriBuku {KategoriBuku.Id}>"
