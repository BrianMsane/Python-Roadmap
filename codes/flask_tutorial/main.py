"""Let's Learn the framework"""

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class MyResource(Resource):
    def get(self):
        return {"message": "This is a get request"}  # return serializable information


api.add_resource(MyResource, "/")


if __name__ == "__name__":
    app.run(debug=True)
