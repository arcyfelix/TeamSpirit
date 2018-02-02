from flask_httpauth import HTTPBasicAuth
from flask import session

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    session['username'] = username
    return session['username'] is not None and session['username'] == 'Woj'