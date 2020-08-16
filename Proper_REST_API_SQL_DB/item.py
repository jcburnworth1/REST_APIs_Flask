## Import libraries
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Proper_REST_API_SQL_DB.database import Database

##################### Example #####################
## All resources must be classes and inherit from Resource class
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
    ## Utilizing reqparse to only allow a price element - We do not want to update name
    parser = reqparse.RequestParser()  ## Use to parse the request
    ## Add specifics that parse will look for / enforce
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank!')

    @jwt_required() ## User must authenticate before calling method
    def get(self, name):  ## Currently allows items of same name
        """
        Take in the name and return the matching item
        :param name: Name of the item
        :return: Corresponding JSON of the item or none if item not found
        """
        ## Setup Connection & Cursor
        connection, cursor = Database.connect_to_db()

        ## Get the data
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        ## Check if anything return
        if row:
            return {'item': {'name': row[0],
                             'price': row[1]}}

        ## Close Connection
        connection.close()

        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        """
        Add the incoming JSON to the items list - {'price': 10.99}
        :param name: {"name": "item"}
        :return: Item that was added
        """
        ## Check if a given item already exists - Error if true
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': f"An item with name '{name}' already exists."}, 400

        data = Item.parser.parse_args()

        item = {'name': name,
                'price': data['price']}
        items.append(item)
        return item, 201  ## Create code

    @jwt_required()
    def delete(self, name):
        """
        Delete the item from item list
        :param name: {"name": "item"}
        :return: {'message': 'Item deleted'}
        """
        global items ## Pulling the items from line 17 down into the function
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        """
        Update or insert a new item to the items list
        :param name: {"name": "item"}
        :return: The item that was updated or inserted
        """
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)

        if item is None:
            item = {'name': name, 'price': data['price']}
        else:
            item.update(data)
        return item

## ItemList Class
class ItemList(Resource):
    def get(self):
        """
        Return all items in the current items list
        :return:
        """
        return {'items': items}