from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from app.config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

client = MongoClient(app.config['MONGO_URI'])
db = client['DB_PIV']

jwt = JWTManager(app)

from app.routes import routes as main_routes
app.register_blueprint(main_routes, url_prefix='/api')

