
from app.extensions import database

class Registered(database.Model):
	__tablename__ = 'Registered'

	NIM = database.Column(database.String(12), primary_key=True)
	password = database.Column(database.String(32), nullable=False)

	def __repr__(self):
		return f"<Registered {self.Id}>"
