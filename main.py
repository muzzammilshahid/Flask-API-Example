from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
port = 5009


class GetSetName(Resource):
    def get(self):
        return {"data": "This is the dummy data of your get request"}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Enter your name')
        args = parser.parse_args(strict=True)
        return {"name": args.get("name")}, 200


api.add_resource(GetSetName, '/api/name')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

