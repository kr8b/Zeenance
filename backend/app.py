import json
from flask import Flask
from flask_cors import CORS
from util.db import db
from flask_jwt_extended import JWTManager


config_file = open('config/dev.json') 
config = json.load(config_file)


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config['JWT_SECRET_KEY'] = config['JWT_SECRET_KEY']
app.config['JWT_BLACKLIST_ENABLED'] = config['JWT_BLACKLIST_ENABLED']

jwt = JWTManager(app)
