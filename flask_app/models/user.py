
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import MySQLConnection

from flask_app.models import user

from flask import flash, session, redirect
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.purchases = []

    # register user
    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW())"
        return connectToMySQL('Exam').query_db(query, data)

    #email check
    @classmethod
    def email_check(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s;"
        results = connectToMySQL('Exam').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

        #grab a single users data
    @classmethod
    def show_one_user(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL('Exam').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


# Static Method  Below #
    # Registration Validator

    @staticmethod
    def validate_register(data):
        email = User.email_check(data)
        is_valid = True
        if len(data['fname']) < 2:
            flash("First name must be 2 or more characters", "register")
            is_valid = False
        if len(data['lname']) < 2:
            flash("Last name must be 2 or more characters", "register")
            is_valid = False
        if email:
            flash("Email is already in use! Please Login!", "register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address! Try Again!", "register")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be 8 or more characters!", "register")
            is_valid = False
        if data['password'] != data['confirmpassword']:
            flash("Passwords do not match! Try again", "register")
            is_valid = False
        return is_valid
