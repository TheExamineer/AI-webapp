from flask import Flask
from flask_cors import CORS
from API.blueprint1.routes import blueprint1
from API.blueprint2.routes import blueprint2


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


app.register_blueprint(blueprint1)
app.register_blueprint(blueprint2)



if __name__ == "__main__":
  app.run()