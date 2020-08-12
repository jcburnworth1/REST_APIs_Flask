## Repo for Reference - https://github.com/tecladocode/rest-api-sections/tree/master/section3
## Import Libraries
from flask import Flask, jsonify, request, render_template

## Create the flask application
app = Flask(__name__)  # '__main__'

## Stores - Used for simplification of our first rest API - Will store in DB later on
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

## Base Route
@app.route('/')
def home():
    return render_template('index.html')

## Post - Used to receive data
## Get - Used to send data back only
## Required Endpoints
## POST /store data: {name} - Create a new store with a given name
@app.route('/store', methods=['POST'])  ## By default, app.route() is a GET request
## methods=['POST'] specifies that this endpoint is only accessible by a POST request
def create_store():
    ## Must be able to access data in the request
    ## Will use postman to send a payload for testing
    ## Capture incoming request and save to a new_store dict
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    ## Add to the stores list
    stores.append(new_store)

    ## Return new store as a confirmation
    return jsonify(new_store)

## GET /store/<string:name> - Return data about a given store
@app.route('/store/<string:name>')
def get_store(name):
    ## Search stores for the corresponding store - If exists return in JSON format
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    ## Error message if store not found
    return jsonify({'Message': 'Store not found'})

## GET /store - Return list of all stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

## POST /store/<string:name>/item {name: price:} - Create an item in a specific store with a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    ## Capture the incoming request
    request_data = request.get_json()

    ## Search for the store - If exists save the new item
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }

            store['items'].append(new_item)

            return jsonify(new_item)

    ## Error message if store not found
    return jsonify({'message': 'store not found'})

## GET /store/<string:name>/item - Return list of items in a given store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])

    ## Error message if store not found
    return jsonify({'message': 'store not found'})

## Execute the program
app.run(port=5000, debug=True)