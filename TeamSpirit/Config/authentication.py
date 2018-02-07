from flask_httpauth import HTTPBasicAuth
from flask import session

# Dealing with BLOB (binary)
import bitarray
# Importing Utils
import sys
sys.path.append('./Utils')
from RequestParser import *
from PasswordEncryption import *


auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(user_mail, password):
    # Defining parameters
    parameters = ['user_mail', 'password']

    # Parsing parameters
    requestParser = RequestParser()
    args = requestParser.parse_parameters_from_array_all_required(parameters)

    user_mail = args['user_mail']
    password = args['password']

    conn = mysql.connection
    cur = conn.cursor()
    sql_query = ''' SELECT USER_PASSWORD FROM USERS WHERE EMAIL = %s ;'''
    cur.execute(sql_query, [user_mail])
    result = cur.fetchone()
    
    # Dealing with empty result
    # That means that the email does not exist in the database
    if(result is None):
        loggedIn = False
    else:
        true_password = result[0]
        password_encryptor = PasswordEncryption()
        loggedIn = password_encryptor.validate_password(password, true_password)
       

    return loggedIn