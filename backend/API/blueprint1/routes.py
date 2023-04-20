from flask import Blueprint , request
from flask_cors import cross_origin
from flask_cors import CORS
from pymongo import MongoClient


uri = "mongodb+srv://user1:1234@cluster0.aacymnc.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client['NEW'] # replace with your database name
collection = db['1ST'] # replace with your collection name

blueprint1 = Blueprint('blueprint1', __name__)
CORS(blueprint1, resources={r"/*": {"origins": "*"}}) #allows to all url access




@blueprint1.route('/submit-enddate', methods=['POST'])
@cross_origin()

def handle_post_request():
    data = request.get_json()
    end_date = data.get('date') # replace 'date' with the name of the input field
   # response_data = {'message': 'Success! Selected date was {}'.format(selected_date)}

    # do something with the selected_date, such as save it to a database or perform calculations
    
   # client.admin.command('ping')
   # print("Pinged your deployment. You successfully connected to MongoDB!")
    # ...

    # return a JSON response with the data to send back to the frontend
   
    return {'message': 'EndDate saved to Backend'}