from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import cross_origin
from pymongo import MongoClient
from pymongo.server_api import ServerApi





uri = "mongodb+srv://kartikmahala56:<XM7HOvpcLFUF4ULK>@cluster0.aacymnc.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['MERN'] # replace with your database name
collection = db['1st-collection'] # replace with your collection name



app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})




@app.route('/submit-date', methods=['POST'])
@cross_origin()
def handle_post_request():
    data = request.get_json()
    selected_date = data.get('date') # replace 'date' with the name of the input field
   # response_data = {'message': 'Success! Selected date was {}'.format(selected_date)}

    # do something with the selected_date, such as save it to a database or perform calculations
    collection.insert_one({'date': selected_date})
    # ...

    # return a JSON response with the data to send back to the frontend
   
    return {'message': 'Date saved to MongoDB'}
if __name__ == "__main__":
  app.run()