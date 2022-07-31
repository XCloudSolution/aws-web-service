# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
import requests


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.


class Offerings(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):

        return jsonify({'offering': [{"type": "DynamoDB", "path": "/dynamodb/"}, {"type": "RDS", "path": "/rds/"}]})

# another resource to calculate the square of a number


class DynamoDB(Resource):

    # Corresponds to POST request
    def post(self):

        data = request.get_json()	 # status code
        return jsonify({'data': data}), 201

    def get(self, id):

        return jsonify({'id': id})


class RDS(Resource):

    # Corresponds to POST request
    def post(self):

        data = request.get_json()	 # status code
        return jsonify({'data': data}), 201

    def get(self, id):

        return jsonify({'id': id})


class Products(Resource):
    def get(self):

        r = requests.get(url="https://fakestoreapi.com/products/")
        return r.json()


# adding the defined resources along with their corresponding urls
api.add_resource(Products, '/products')
api.add_resource(Offerings, '/')
api.add_resource(DynamoDB, '/dynamodb/<int:id>', endpoint='dynamodb')
api.add_resource(RDS, '/rds/<int:id>', endpoint='rds')


# driver function
if __name__ == '__main__':

    app.run(debug=True)
