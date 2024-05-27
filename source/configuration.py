import os
import secrets
base_directory: str = os.path.abspath(os.path.dirname(__file__))

DATABASE_FILE_NAME: str = 'library.db'


class Configuration:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_directory, DATABASE_FILE_NAME)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = secrets.token_hex(16)