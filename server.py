from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import items
from flask_app.controllers import crystals

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
