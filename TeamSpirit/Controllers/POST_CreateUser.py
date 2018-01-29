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

class Post_CreateUser(Resource):
    # def post(self):
    def get(self):
        
        # Defining parameters
        parameters = ['firstName', 'surname', 'password']

        # Parsing parameters
        requestParser = RequestParser()
        args = requestParser.parse_parameters_from_array_all_required(parameters)

        firstName = args['firstName']
        surname = args['surname']
        password = args['password']
        
        # MySQL Connection
        conn = mysql.connection
        cur = conn.cursor()
        sql_query = ''' INSERT INTO USERS
                        (FIRST_NAME,
                        SURNAME,
                        USER_PASSWORD,
                        CREATED_DATETIME)
                        VALUES
                        (%s,
                        %s,
                        %s,
                        SYSDATE()) ;'''
        cur.execute(sql_query, [firstName, surname, password])
        conn.commit()
        
        return {'status' : 'success'}, 200
api.add_resource(Post_CreateUser, '/POST/CreateUser/')