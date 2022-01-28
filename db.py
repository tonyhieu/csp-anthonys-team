from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app 

dbURI = 'sqlite:///model/games.db'
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Games(db.Model):
    gameID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=False, nullable=False)
    author = db.Column(db.String(255), unique=False, nullable=False)
    embed = db.Column(db.String(255), unique=False, nullable=False)


    def __init__ (self, title, author, embed):
        self.title = title
        self.author = author
        self.embed = embed
    
    def create(self):
        try:
            db.session.add(self)  
            db.session.commit()  
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {
            "gameID": self.gameID,
            "title": self.title,
            "author": self.author,
            "embed": self.embed
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, title="", author="", embed=""):
        if len(title) > 0:
            self.title = title
        if len(author) > 0:
            self.author = author
        if len(embed) > 0:
            self.embed = embed
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def create_db():
    db.create_all()

    g1 = Games(title='Dabbing Tycoon', author='Anthony Vo', embed='<iframe src="https://scratch.mit.edu/projects/199615756/embed" allowtransparency="true" width="700" height="700" frameborder="0" scrolling="no" allowfullscreen></iframe>')

    table = [g1]
    for game in table:
        try:
            db.session.add(game)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print("stop trying to do the same thing twice")

if __name__ == "__main__":
    create_db()

