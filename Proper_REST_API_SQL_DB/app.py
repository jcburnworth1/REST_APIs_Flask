## Reference Code - https://github.com/tecladocode/rest-api-sections/tree/master/section5
## Import Libraries
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Proper_REST_API_SQL_DB.user import UserRegister
from Proper_REST_API_SQL_DB.item import Item, ItemList
from Proper_REST_API_SQL_DB.security import authenticate, identity

## Create the flask application
app = Flask(__name__)  # '__main__'
app.secret_key = 'lala' ## If prod API, this would need to be a real key
api = Api(app)  ## Allow for easy resource addition with GET, POST, DELETE, etc.

## Return JWT token for auth later on
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity) #/auth

## Dummy list of dicts for items - Will setup a DB in a later project
# items = [] - See database for items

## Resources
api.add_resource(Item, '/item/<string:name>')  ## http://127.0.0.1:5000/item/chair
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

## Execute the program
app.run(port=5000, debug=True)
