"""Let's learn the Flask framework"""

from flask import Flask
from flask_restful import Api
from resources.users import Users
from resources.videos import Video

app = Flask(__name__)
api = Api(app)


api.add_resource(Users, "/users/<int: id>")
api.add_resource(Video, "/videos/<string: id>")


if __name__ == "__main__":
    app.run(debug=True)
