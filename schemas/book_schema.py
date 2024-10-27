from marshmallow import fields
from schemas.schemas import ma
from models.book import Book

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True  # Charge directement les instances du modèle
    
    title = fields.Str(required=True)
    description = fields.Str()
    publication_date = fields.Date(format='%Y-%m-%d')  # Gère la conversion de chaîne à date
    author_id = fields.Int(required=True)