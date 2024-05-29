import os
import secrets
base_directory: str = os.path.abspath(os.path.dirname(__file__))

DATABASE_FILE_NAME: str = 'library.db'


class Configuration:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_directory, DATABASE_FILE_NAME)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	##SECRET_KEY = b'\xf1\x85\x19\xd2\xc3\xe2\xd3\x15\x8b\xb8\xfb\xe7\x1f\xda\xe1\xed'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
