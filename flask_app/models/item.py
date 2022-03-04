from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import MySQLConnection


class Item:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.attributes = data['attributes']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * from items"
        results = connectToMySQL('project').query_db(query)
        items = []
        if not results:
            return "Error"
        for thing in results:
            items.append(cls(thing))
        return items

    @classmethod
    def get_four(cls):
        query = "SELECT * from items LIMIT 4"
        results = connectToMySQL('project').query_db(query)
        items = []
        if not results:
            return "Error"
        for thing in results:
            items.append(cls(thing))
        return items

    @classmethod
    def get_one(cls, data):
        query = "SELECT * from items WHERE id = %(id)s"
        result = connectToMySQL('project').query_db(query, data)
        this_item = Item(result[0])
        return this_item

    @classmethod
    def add_item(cls, data):
        query = "INSERT into items (name, attributes, description, created_at, updated_at) VALUES (%(name)s, %(attributes)s, %(description)s, now(), now())"
        return connectToMySQL('project').query_db(query, data)

    @classmethod
    def update_item(cls, data):
        query = "UPDATE project.items SET name = %(name)s, attributes = %(attributes)s, description = %(description)s, updated_at = now() WHERE id = %(id)s"
        return connectToMySQL('project').query_db(query, data)
