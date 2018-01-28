from flask_restplus import Resource

from flask import jsonify
from app import *
from Config.authentication import *

class Get_All_Tasks(Resource):
    @auth.login_required
    def get(self):
        # MySQL Cursor ~ Connection
        cur = mysql.connection.cursor()
        cur.execute(''' SELECT * FROM TASK;''')
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

api.add_resource(Get_All_Tasks, '/GET/AllTasks/')

