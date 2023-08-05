from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('message', type=str)
parser.add_argument('reciever', type=str)

class Auth(Resource):
    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()
        username = str(args['username'])  
        response = jsonify(dict(error='User Already Logged In'))
        response.status_code = 409
        return response

api.add_resource(Auth, "/some/som2")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234 ,debug=True)