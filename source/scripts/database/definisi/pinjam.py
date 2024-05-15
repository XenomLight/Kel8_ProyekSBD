
from ..database import database

class Pinjam(database.Model):
	__tablename__ = 'Pinjam'

	Id = database.Column(database.Integer, primary_key=True, autoincrement=True)
	IdBuku = database.Column(database.Integer, database.ForeignKey('Buku.Id'), nullable=False)
	NIM = database.Column(database.String(12), database.ForeignKey('Mahasiswa.NIM'), nullable=False)
	TanggalPeminjaman = database.Column(database.DateTime, nullable=False)
	TanggalPengembalian = database.Column(database.DateTime, default=None)
	Status = database.Column(database.Enum('Aktif', 'Selesai', 'Melewati Tenggat'))

	def __repr__(self):
		return f"<Pinjam {Pinjam.Id}>"
