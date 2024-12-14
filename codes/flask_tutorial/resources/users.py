from flask_restful import Resource
from data import user_data


class Users(Resource):
    def get(self, id):
        return [user for user in user_data.keys() if user == id][0]

    def post(self, id):
        return {"message": "this is a post request"}
