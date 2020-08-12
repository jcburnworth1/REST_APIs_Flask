## Reference Code - https://github.com/tecladocode/rest-api-sections/tree/master/section4
## Import Libraries #####
from flask import Flask
from flask_restful import Resource, Api

## Create the flask application
app = Flask(__name__)  # '__main__'
api = Api(app) ## Allow for easy resource addition with GET, POST, DELETE, etc.

## All resources must be classes and inherit from Resource class
class Student(Resource):
    ## Resource that can only be access with a GET method
    def get(self, name):
        return {'student': name}

## Add student resource
api.add_resource(Student, '/student/<string:name>') ## http://127.0.0.1:5000/student/JC

## Execute the program
app.run(port=5000, debug=True)