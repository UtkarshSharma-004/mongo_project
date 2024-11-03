from marshmallow import schema, fields

class cartoonSchema(schema):
    cartoon_name=fields.Str(required=True)
    genre= fields.Str(required=True)
    creator=fields.Str(required=False)
    year=fields.Date()

__all__ = ["cartoonSchema"]