from flask import Blueprint , request, jsonify
from flask_cors import cross_origin
from flask_cors import CORS
from pymongo import MongoClient


import csv


uri = "mongodb+srv://user1:1234@cluster0.aacymnc.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client['NEW'] # replace with your database name
collection = db['1ST'] # replace with your collection name

blueprint2 = Blueprint('blueprint2', __name__)
CORS(blueprint2, resources={r"/*": {"origins": "*"}})





@blueprint2.route('/upload-csv', methods=['POST'])

@cross_origin()

def handle_post_request():
    csv_file = request.files['csv']
    csv_data = csv_file.read().decode('utf-8')

    # Parse the CSV data using the csv module
    csv_reader = csv.reader(csv_data.splitlines())
    data = []
    for row in csv_reader:
        data.append(row)
    # Save the CSV data to the MongoDB collection
    for row in data:
        doc = {
            "img_id": row[0],
            "object": row[1],
            "date": row[2]
        }
        collection.insert_one(doc)
   

    return jsonify({'message': 'csv saved to database successfully!'})