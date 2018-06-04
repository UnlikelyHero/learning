from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'don'
api = Api(app)

# allows authentication of users
jwt = JWT(app, authenticate, identity)  # /auth

# initialize items list
items = []


# functions that handle working with specific items
class Item(Resource):
    # specifies which values from the body are considered
    # extraneous values are discarded including 'item_id'
    # 'item_id' should only be passed in as a url argument.
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name"
    )
    parser.add_argument(
        "price",
        type=float
    )

    @jwt_required()
    def get(self, item_id):
        item = next(filter(lambda x: x['item_id'] == item_id, items), None)
        if item:
            return {
                "item": item
            }, 200
        else:
            return {
                "message": "The item id, {} was not found.".format(item_id)
            }, 404

    @jwt_required()
    def put(self, item_id):
        item = next(filter(lambda x: x['item_id'] == item_id, items), None)
        if item:
            data = Item.parser.parse_args()
            item.update(data)
            return {
                "message": "Item {} has been updated with the following data".format(item_id),
                "item": item
            }, 200
        else:
            return {
                "message": "The item you're referencing does not exist."
            },

    @jwt_required()
    def delete(self, item_id):
        global items
        item = next(filter(lambda x: x['item_id'] == item_id, items), None)
        if item:
            items = list(filter(lambda x: x['item_id'] != item_id, items))
            return {
                "message": "The item, {} has been deleted".format(item_id)
            }, 200
        else:
            return {
                "message": "The item you're referencing does not exist."
            }


# functions to query and create items
class ItemList(Resource):
    # specifies which values from the body are considered
    # specified values are all meant to be required
    # extraneous values are discarded
    parser = reqparse.RequestParser()
    parser.add_argument(
        "item_id",
        required=True,
        help="Your item must have a unique 'item_id' value."
    )
    parser.add_argument(
        "name",
        required=True,
        help="Your item must have a name."
    )
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="Your item must have a price."
    )

    @jwt_required()
    def get(self):
        # returns the list of items, sorted by item_id value
        return {'items': sorted(items, key=lambda x: x['item_id'])}

    @jwt_required()
    def post(self):
        data = ItemList.parser.parse_args()
        item = next(
            filter(lambda x: x['item_id'] == data['item_id'], items),
            None
        )
        if item:
            return {
                "message": "The 'item_id' value must be unique. {} already exists".format(data['item_id'])
            }, 400
        else:
            new_item = {
                "item_id": data['item_id'],
                "name": data['name'],
                "price": data['price']
                }
            items.append(new_item)
            return new_item, 201


## Resources ##
api.add_resource(Item, '/items/<string:item_id>')
# endpoint works with specific items
api.add_resource(ItemList, '/items')
# endpoint lists items or adds a new item.


# app initialization
app.run(port=5000, debug=True)
