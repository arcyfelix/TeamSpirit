from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# Importing Controllers
from Controllers.HelloWorld import HelloWorld


api.add_resource(HelloWorld, '/')


app.run(debug=True)