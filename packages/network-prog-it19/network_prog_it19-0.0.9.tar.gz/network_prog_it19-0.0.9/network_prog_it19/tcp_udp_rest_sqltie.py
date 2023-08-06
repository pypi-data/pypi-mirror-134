import socket
import pickle

from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

from sqlite3 import *

host = "127.0.0.1"
MAX_BYTES = 65326

def serverUDP(port): #UDP
    sock = socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    data, adress = sock.recvfrom(MAX_BYTES)
    # pickle.dumps()
    # pickle.loads()
    sock.sendto("message", adress)

def clientUDP(port): #TCP
    sock = socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendTo("message", (host, port))
    data, adress = sock.recvfrom(MAX_BYTES)

def serverTCP(port):
    sock = socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,  socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    sc, address = sock.accept()

    data = sc.recv(MAX_BYTES)

    sc.sendall(b"message")

def clientTCP(port):
    sock = socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(b"aaa")
    sock.recvfrom(MAX_BYTES)


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument("username", type=str)

class Some(Resource):
    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()
        response = jsonify(dict(s=""))
        return response

class Some2(Resource):
    def get(self, some_thing):
        request.get_json(force=True)
        parser.get_args()
        response = jsonify(dict(s=""))
        return response

api.add_resource(Some, "path/to/it")

api.add_resource(Some2, "path/to/<int:some_thing>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1234", debug=True)
    ofile = open("", "w+")
    ofile.readlines()
    ofile.write()
    ofile.close()

    conn = connect("file.db")
    cr = conn.cursor()
    cr.execute("select * from ?", ["aaa"])
    rows = cr.fetchall()