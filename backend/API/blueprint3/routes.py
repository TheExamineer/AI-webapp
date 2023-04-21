from flask import Blueprint , request, jsonify, current_app
from flask_cors import cross_origin
from flask_cors import CORS
from pymongo import MongoClient
import base64

uri = "mongodb+srv://user1:1234@cluster0.aacymnc.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client['NEW'] # replace with your database name
collection = db['1ST'] # replace with your collection name

blueprint3 = Blueprint('blueprint3', __name__)
CORS(blueprint3, resources={r"/*": {"origins": "*"}})

@blueprint3.route('/get-data')
@cross_origin()
def get_data():
    # Get the start and end dates from the query parameters
    result1 = collection.find_one()
    if result1:
       
        start_date =   result1.get('start_date')
       
    else:
        return {'message': 'Dindt Find Start/End/Both '}
    result2 = collection.find_one()
    if result2: 
        end_date =   result2.get('end_date') 
    else:
        return {'message': 'Fucked by end date '}
    
    print(start_date)
    print(end_date)
    # Query the MongoDB collection to get the data
    data = collection.find({'date': {'$gte': start_date, '$lte': end_date}}, {'_id': False})

    # Create a list of dictionaries to hold the data
    response_data = []

    # Iterate over the MongoDB data and append the required fields to the response data
    for i,doc in data:
        with open(f'../../images/{doc["img_id"]}.jpg', 'rb') as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
        response_data.append({
            'index': i + 1,
            'img_id': doc['img_id'],
            'object': doc['object'],
            'img':   encoded_string
        })
        for i,doc in data:
            print("Document found:", doc)
      

    # Return the response data as JSON
    return jsonify(response_data)