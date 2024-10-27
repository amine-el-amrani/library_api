from models.db import db

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.String(255))
    birth_date = db.Column(db.Date)


    books = db.relationship('Book', back_populates='author')