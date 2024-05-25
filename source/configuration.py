import os

base_directory: str = os.path.abspath(os.path.dirname(__file__))

DATABASE_FILE_NAME: str = 'library.db'


class Configuration:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_directory, DATABASE_FILE_NAME)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
