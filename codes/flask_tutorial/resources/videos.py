from flask_restful import Resource, reqparse
from data import video_data
from jsonschema import validate, ValidationError

video_args = reqparse.RequestParser()
video_args.add_argument("name", type=str, help="the name of the video", required=True)
video_args.add_argument("views", type=int, help="the number of views", required=True)
video_args.add_argument("likes", type=int, help="the number of likes", required=True)

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "views": {"type": "integer"},
        "likes": {"type": "integer"},
    },
    "required": ["name", "likes", "views"],
}


class Video(Resource):
    def get(self, id):
        return video_data[id]

    def post(self, id):
        args = video_args.parse_args()
        try:
            validate(instance=args, schema=schema)
        except ValidationError as err:
            raise TypeError(f"The schema is invalid: {err}")
        else:
            return {id: args}

    def delete(self, id):
        pass

    def put(self, id):
        pass
