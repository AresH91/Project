from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import MySQLConnection


class Crystal:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.attributes = data['attributes']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # class methods

    @classmethod
    def get_all(cls):
        query = "SELECT * from crystals ORDER BY name"
        results = connectToMySQL('project').query_db(query)
        gems=[]
        if not results:
            return "Error"
        for rocks in results:
            gems.append(cls(rocks))
        return gems

    @classmethod
    def get_four(cls):
        query = "SELECT * from crystals LIMIT 4"
        results = connectToMySQL('project').query_db(query)
        gems = []
        if not results:
            return "Error"
        for rocks in results:
            gems.append(cls(rocks))
        return gems

    @classmethod
    def get_one(cls, data):
        query = "SELECT * from crystals WHERE id = %(id)s"
        result = connectToMySQL('project').query_db(query, data)
        this_crystal = Crystal(result[0])
        return this_crystal

    @classmethod
    def add_crystal(cls, data):
        query = "INSERT into crystals (name, attributes, description, created_at, updated_at) VALUES (%(name)s, %(attributes)s, %(description)s, now(), now())"
        return connectToMySQL('project').query_db(query, data)

    @classmethod
    def update_crystal(cls, data):
        query = "UPDATE project.crystals SET name = %(name)s, attributes = %(attributes)s, description = %(description)s, updated_at = now() WHERE id = %(id)s"
        return connectToMySQL('project').query_db(query, data)
