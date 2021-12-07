from flask_sqlalchemy import SQLAlchemy
from app import app 

dbURI = 'sqlite:///model/games.db'
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI

db = SQLAlchemy(app)

class Games(db.model):
    gameID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))