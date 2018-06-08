import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


## Resources ##


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

        if UserModel.find_by_username(data['username']):
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
