import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


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

    # @jwt_required()
    def get(self, item_id):
        item = ItemModel.find_by_item_id(item_id)

        if item:
            return item
        return {
            "message": "The item_id, {} was not found.".format(item_id)
        }, 404

    @jwt_required()
    def put(self, item_id):
        item = ItemModel.find_by_item_id(item_id)
        if item:
            data = Item.parser.parse_args()
            updated_item = {
                "item_id": item_id,
                "name": data['name'],
                "price": data['price']
            }
            try:
                ItemModel.update_item(updated_item)
            except():
                return {
                    "message": "An error occurred when trying to insert the item."
                }, 500

            return {
                "message": "Item {} has been updated with the following data".format(item_id),
                "item": updated_item
            }, 200
        return {
            "message": "The item you're referencing does not exist."
        },

    @jwt_required()
    def delete(self, item_id):
        if ItemModel.find_by_item_id(item_id):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "DELETE FROM items WHERE item_id=?"
            cursor.execute(query, (item_id,))

            connection.commit()
            connection.close()
            return {
                "message": "The item, {} has been deleted".format(item_id)
            }, 201
        return {
            "message": "The item you're referencing does not exist."
        }, 404


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

    # @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items ORDER BY item_id ASC"
        result = cursor.execute(query)
        items = []
        for row in result:
            new_row = {
                "item_id": row[0],
                "name": row[1],
                "price": row[2]
            }
            items.append(new_row)
        connection.close()
        return items, 200

    @jwt_required()
    def post(self):
        data = ItemList.parser.parse_args()

        if Item.find_by_item_id(data['item_id']):
            return {
                "message": "The 'item_id' value must be unique. {} already exists".format(data['item_id'])
            }, 400

        new_item = {
            "item_id": data['item_id'],
            "name": data['name'],
            "price": data['price']
        }
        try:
            Item.insert_item(new_item)
        except():
            return {
                "message": "An error occurred when trying to insert the item."
            }, 500

        return {
            "message": "Item '{}' has been created".format(new_item['item_id']),
            "item": new_item
        }, 201
