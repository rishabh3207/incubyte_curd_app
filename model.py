from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class Words(db.Model):
    __tablename__ = "words"
 
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(), unique = True)
 
    def __init__(self, word):
        self.word = word
