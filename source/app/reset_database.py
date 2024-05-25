
# jalani di flask shell untuk reset file database "library.db"

from app.extensions import database

from app.buku.database.buku.definisi import Buku
from app.buku.database.dikategorikan.definisi import Dikategorikan
from app.buku.database.kategori_buku.definisi import KategoriBuku
from app.buku.database.pengarang.definisi import Pengarang
from app.buku.database.penerbit.definisi import Penerbit
from app.buku.database.rak.definisi import Rak

from app.mahasiswa.database.mahasiswa.definisi import Mahasiswa

from app.pinjam.database.pinjam.definisi import Pinjam

database.drop_all()
database.create_all()
