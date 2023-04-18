from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/getting-data', methods=['POST'])
@cross_origin()
def handle_post_request():
    data = request.get_json()
    selected_date = data.get('date') # replace 'date' with the name of the input field

    # do something with the selected_date, such as save it to a database or perform calculations
    # ...

    # return a JSON response with the data to send back to the frontend
    response_data = {'message': 'Success! Selected date was {}'.format(selected_date)}
    return jsonify(response_data), 200
if __name__ == "__main__":
  app.run()