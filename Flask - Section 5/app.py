from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister, Users
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'don'
api = Api(app)

# allows authentication of users
jwt = JWT(app, authenticate, identity)  # /auth


## Resources ##
api.add_resource(Item, '/items/<string:item_id>')
# endpoint works with specific items
api.add_resource(ItemList, '/items')
# endpoint lists items or adds a new item.
api.add_resource(UserRegister, '/register')
# endpoint simply pulls up a list of users.
api.add_resource(Users, '/users')


# app initialization
app.run(port=5000, debug=True)
