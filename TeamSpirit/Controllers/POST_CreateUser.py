# Importing Flask and Flask_Restplus
from flask_restplus import Resource
from flask import jsonify

# Importing the App and Authentication
from app import *
from Config.authentication import *

# Importing Utils
import sys
sys.path.append('./Utils')
from RequestParser import *
from PasswordEncryption import *

class Post_CreateUser(Resource):
    # def post(self):
    def get(self):
        
        # Defining parameters
        parameters = ['firstName', 'surname', 'email', 'password']

        # Parsing parameters
        requestParser = RequestParser()
        args = requestParser.parse_parameters_from_array_all_required(parameters)

        firstName = args['firstName']
        surname = args['surname']
        email = args['email']
        password = args['password']
        
        # Salt and Hash the password
        password_encryptor = PasswordEncryption()

        encrypted_password = password_encryptor.encrypt_password(password)

        # MySQL Connection
        conn = mysql.connection
        cur = conn.cursor()
        sql_query = ''' INSERT INTO USERS
                        (FIRST_NAME,
                        SURNAME,
                        EMAIL, 
                        USER_PASSWORD,
                        CREATED_DATETIME)
                        VALUES
                        (%s,
                        %s,
                        %s,
                        %s,
                        SYSDATE()) ;'''
        cur.execute(sql_query, [firstName, surname, email, encrypted_password])
        conn.commit()
        
        return {'status' : 'success'}, 200
api.add_resource(Post_CreateUser, '/POST/CreateUser/')