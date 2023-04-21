from flask import Flask
from flask_cors import CORS
from API.blueprint1.routes import blueprint1
from API.blueprint2.routes import blueprint2
from API.blueprint3.routes import blueprint3
from API.blueprint4.routes import blueprint4
from API.blueprint5.routes import blueprint5


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


app.register_blueprint(blueprint1)
app.register_blueprint(blueprint2)
app.register_blueprint(blueprint3)
app.register_blueprint(blueprint4)
app.register_blueprint(blueprint5)





if __name__ == "__main__":
  app.run()