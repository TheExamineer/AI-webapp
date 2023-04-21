from flask import Blueprint , request
from flask_cors import cross_origin
from flask_cors import CORS
from pymongo import MongoClient


uri = "mongodb+srv://user1:1234@cluster0.aacymnc.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client['NEW'] # replace with your database name
collection = db['1ST'] # replace with your collection name

blueprint4 = Blueprint('blueprint4', __name__)
CORS(blueprint4, resources={r"/*": {"origins": "*"}}) #allows to all url access




@blueprint4.route('/submit-startdate', methods=['POST'])
@cross_origin()

def handle_post_request():
    data = request.get_json()
    start_date = data.get('date') 
   
     # Store the variable in MongoDB
    collection.insert_one({'start_date': start_date})
   
    return {'message': 'StartDate saved to backend'}