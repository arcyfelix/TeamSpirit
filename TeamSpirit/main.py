"""
This script runs the server
"""
from os import environ

# Login and logout
from Controllers.Login.login import login

# Importing Controllers
from Controllers.GET_AllTasks import *
from Controllers.GET_TaskForGivenTaskId import *
from Controllers.POST_CreateUser import *

# Run the server
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)
    sess = Session()
    sess.init_app(app)