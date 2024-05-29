from sqlalchemy import text

from app.extensions import database

from app.auth.database.registered.definisi import Registered
from app.auth.database.registered import manipulasi


def register_route(request_form):


	manipulasi.register(
		request_form["NIM"],
		request_form["password"],
	)
 
def login_route(request_form):
    
    manipulasi.validasi_akun(
        request_form["NIM"],
        request_form["password"],

    )