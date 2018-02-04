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

class Get_TaskForGivenTaskId(Resource):   
    
    def get(self):
        if not session.get('user_mail') == None:
            if session['user_mail'] == 'wor@kth.se':
                # Defining parameters
                parameters = ['id']

                # Parsing parameters
                requestParser = RequestParser()
                args = requestParser.parse_parameters_from_array_all_required(parameters)

                # MySQL 
                conn = mysql.connection
                cur = conn.cursor()
                sql_query = ''' SELECT * FROM TASKS WHERE TASK_ID = %s ;'''
                cur.execute(sql_query, [int(args['id'])])
                result = cur.fetchall()
        
                # Defining result JSON
                columns = ['id', 'description', 'planned_date_start', 'planned_time_start']
                column_index = [0, 1, 5, 6]

                return_json = {}
                for i, column in zip(column_index, columns) :
                    data = [str(row[i]) for row in result]
                    return_json[column] = data
        
                response = jsonify({'status' : 'success', 'response': return_json})
                response.status_code = 200
                return response
        else:
            return jsonify({'message' : 'Please log in!'})

api.add_resource(Get_TaskForGivenTaskId, '/GET/TaskForGivenTaskId/')