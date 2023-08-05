from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('message', type=str)
parser.add_argument('reciever', type=str)

class AuthPost(Resource):
    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()
        username = str(args['username'])  
        response = jsonify(dict(error='User Already Logged In'))
        response.status_code = 409
        return response

class AuthGet(Resource):
    def get(self, product_id):
        # request.get_json(force=True)
        # args = parser.parse_args()
        # username = str(args['username'])  
        response = jsonify(dict(error='User Already Logged In'))
        response.status_code = 409
        return response

api.add_resource(AuthPost, "/some/some2")

api.add_resource(AuthGet, "/some/<int:product_id>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234 ,debug=True)