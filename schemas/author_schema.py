from marshmallow import fields
from schemas.schemas import ma
from models.author import Author

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
    
    name = fields.Str(required=True)
    biography = fields.Str()
    birth_date = fields.Date(format='%Y-%m-%d')