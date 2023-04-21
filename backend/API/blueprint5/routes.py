from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from pymongo import MongoClient
from flask_cors import cross_origin
from flask_cors import CORS




# connect to your MongoDB cluster
uri = "mongodb+srv://user1:1234@cluster0.aacymnc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client['NEW'] # replace with your database name
collection = db['1ST'] # replace with your collection name

blueprint5 = Blueprint('blueprint5', __name__)
CORS(blueprint5, resources={r"/*": {"origins": "*"}}) #allows to all url access


@blueprint5.route('/delete-all', methods=['DELETE'])
@cross_origin()


def delete_all():
    collection.delete_many({})
    return jsonify({'message': 'All documents deleted successfully'})


