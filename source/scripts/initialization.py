
# langkah-langkah menyiapkan aplikasi untuk jalan

from .app import app
from .database.database import database

def intialize():
	app.run(debug=True)
	print("Sup")


def main():
	pass


if __name__ == "__main__":
	main()
