from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # instancia de la app flask

# Configuracion de la db con sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

