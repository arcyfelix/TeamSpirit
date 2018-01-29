from flask_restplus import Resource

from flask_restplus import reqparse
from flask import jsonify

from app import *
from Config.authentication import *

class Get_TaskForGivenTaskId(Resource):   
    @auth.login_required
    def get(self):
        # MySQL Cursor ~ Connection
        parser = reqparse.RequestParser()
        parser.add_argument('id', 
							type = int, 
							location = 'args', 
							required = True,  
							help = 'ID of the task')
        args = parser.parse_args()
        
        cur = mysql.connection.cursor()
        sql_query = ''' SELECT * FROM TASK WHERE TASK_ID = %s ;'''
        cur.execute(sql_query, [int(args['id'])])
        result = cur.fetchall()
        
        columns = ['id', 'description', 'planned_date_start', 'planned_time_start']
        column_index = [0, 1, 5, 6]

        return_json = {}
        for i, column in zip(column_index, columns) :
            data = [str(row[i]) for row in result]
            return_json[column] = data
        
        response = jsonify(return_json)
        response.status_code = 200
        return response

api.add_resource(Get_TaskForGivenTaskId, '/GET/TaskForGivenTaskId/')