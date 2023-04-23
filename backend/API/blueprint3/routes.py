from flask import Blueprint , request, jsonify, current_app
from flask_cors import cross_origin
from flask_cors import CORS
from pymongo import MongoClient
import base64
import os

uri = "mongodb+srv://user1:1234@cluster0.aacymnc.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the serveruser1:1234
client = MongoClient(uri)
db = client['NEW'] # replace with your database name
collection = db['1ST'] # replace with your collection name

blueprint3 = Blueprint('blueprint3', __name__)
CORS(blueprint3, resources={r"/*": {"origins": "*"}})

@blueprint3.route('/get-data')
@cross_origin()
def get_data():
    # Get the start and end dates from the query parameters
       # result = collection.find()
   
       
        cursor = collection.find()
        for document in cursor:
            end_date = document.get("end_date")
            print('Value of end_date:', end_date)
            if end_date is not None:
                break   
        
        
        cursor1 = collection.find()
        for document in cursor1:
            start_date = document.get("start_date")  
            print('Value of start_date:', start_date)  
            if start_date is not None :
                break
            
        
           # if start_date is not None and end_date is not None:
            #    print('Value of end_date:', end_date)
             #   print('Value of start_date:', start_date)
              

        
    # Query the MongoDB collection to get the data
               # collection.delete_many({start_date: {'$exists': True}})
               # collection.delete_many({end_date: {'$exists': True}})
        query = {"date": {'$gte': start_date, '$lte': end_date}}
        print('Query:', query)
        data = collection.find(query, {'_id': False})
       # num_docs = len(data)
      #  print(f"Number of documents found: {num_docs}")
      #  for doc in data:
      #      print(doc)

        
# Create a list of dictionaries to hold the data
        response_data = []
        response_data.append({
            'start_date': start_date,
            'end_date':end_date
        })
        
        
        

# Iterate over the MongoDB data and append the required fields to the response data
        for i,doc in enumerate(data):
            
            with open(f'./images/{doc["img_id"]}', 'rb') as img_file:
                    encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
                    response_data.append({
                        'index': i + 1,
                        'img_id': doc['img_id'],
                        'object': doc['object'],
                        'img':   encoded_string
                        
                    })
            print(response_data[0]['start_date'])
            print(response_data[0]['end_date'])

        if response_data:
            return jsonify(response_data),200
        else:
            error_message = {'message': 'No documents found based on the specified keys'}
            return jsonify(error_message), 405
         #   else:
          #      error_message = {'message': 'Start date and/or end date not found in database'}
           #     return jsonify(error_message), 408
    
      
       

    
    
  
      

    