import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))  # intended tuple
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))  # intended tuple
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="A username is required for this request"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="A password is required for this request"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {
                "message": "The user, '{}' already exists".format(data['username'])
            }, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection. close()

        return {
            "message": "User '{}' was created successfully.".format(data['username'])
        }, 201


class Users(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users ORDER BY id ASC"
        result = cursor.execute(query)
        users = []
        for row in result:
            new_row = {
                "id": row[0],
                "username": row[1],
                "password": "***"
            }
            users.append(new_row)
        connection.close()
        return users, 200
