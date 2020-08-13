## Reference Code - https://github.com/tecladocode/rest-api-sections/tree/master/section4
## Import Libraries
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity

## Create the flask application
app = Flask(__name__)  # '__main__'
app.secret_key = 'lala' ## If prod API, this would need to be a real key
api = Api(app)  ## Allow for easy resource addition with GET, POST, DELETE, etc.

## Dummy list of dicts for items - Will setup a DB in a later project
items = [
    {'name': 'test item',
     'price': 9.99}
]

## All resources must be classes and inherit from Resource class
##################### Example #####################
## Student Class / Resource
# class Student(Resource):
#     ## Resource that can only be access with a GET method
#     def get(self, name):
#         return {'student': name}

## Add student resource
# api.add_resource(Student, '/student/<string:name>') ## http://127.0.0.1:5000/student/JC
###################################################

## Item Class
class Item(Resource):
    def get(self, name):  ## Currently allows items of same name
        """
        Take in the name and return the matching dict
        :param name: Name of the item
        :return: Corresponding JSON of the item or none if item not found
        """
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        """
        Add the incoming JSON item to the items list
        :param name: {"name": "item": "price": 9.99}
        :return: Item that was added
        """
        ## Check if a given item already exists
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': f"An item with name '{name}' already exists."}, 400
        request_data = request.get_json() ## This will error if content is not JSON

        item = {'name': name,
                'price': request_data['price']}
        items.append(item)
        return item, 201  ## Create code

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

## ItemList Class
class ItemList(Resource):
    def get(self):
        """
        Return all items in the current items list
        :return:
        """
        return {'items': items}


## Resources
api.add_resource(Item, '/item/<string:name>')  ## http://127.0.0.1:5000/student/JC
api.add_resource(ItemList, '/items')

## Execute the program
app.run(port=5000, debug=True)
