import sqlite3


class ItemModel:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def json(self):
        return{"item_id": self.item_id, "name": self.name, "price": self.price}

    def find_by_item_id(self):
        connection = sqlite3.connect('data.db')
        # item = next(filter(lambda x: x['item_id'] == item_id, items), None)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items where item_id=?"
        result = cursor.execute(query, (self.item_id,))

        row = result.fetchone()
        connection.close()

        if row:
            return {"item_id": row[0], "name": row[1], "price": row[2]}

    def insert_item(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?, ?)"
        cursor.execute(query, (self['item_id'], self['name'], self['price']))

        connection.commit()
        connection.close()

    def update_item(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET name=?, price=? WHERE item_id=?"
        cursor.execute(query, (self['name'], self['price'], self['item_id']))

        connection.commit()
        connection.close()
