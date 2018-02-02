from flask import Flask
from flask_restful import Api
from flask_mysqldb import MySQL


def app():
    app = Flask(__name__)
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'memcached'
    api = Api(app)

    # Configuration
    from Config.database_connection import configure_connection
    configure_connection(app)
    mysql = MySQL(app)
    return app, mysql, api

# Initialize Flask App, MySQL connector and API handler
app, mysql, api = app()
