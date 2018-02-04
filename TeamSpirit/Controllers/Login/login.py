# Importing Flask and Flask_Restplus
from flask_restplus import Resource
from flask import jsonify, session

# Importing the App and Authentication
from app import *

# Importing Utils
import sys
sys.path.append('./Utils')
from RequestParser import *

class login(Resource):
    # def post(self):
    def get(self):
         # Defining parameters
        parameters = ['user_mail', 'password']

        # Parsing parameters
        requestParser = RequestParser()
        args = requestParser.parse_parameters_from_array_all_required(parameters)

        user_mail = args['user_mail']
        password = args['password']

        # Setting up session
        session['user_mail'] = user_mail
        session['loggedIn'] = True

        return jsonify(str(session))

        

api.add_resource(login, '/login/')