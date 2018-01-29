"""
This script runs the server
"""
from os import environ


# Importing Controllers
from Controllers.GET_AllTasks import *
from Controllers.GET_TaskForGivenTaskId import *

# Run the server
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)
