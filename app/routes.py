from flask import Blueprint, request, jsonify
from .db import get_db
from config import setup_logging
from .models.cartoon_schema import cartoonSchema
from marshmallow import ValidationError

logger=setup_logging()

main=Blueprint('main',__name__)

db=get_db()

obj_collection=db['CARTOON']


# create the schema instance

cartoon_Schema= cartoonSchema()
cartoonsSchema= cartoonSchema(many=True)


@main.route('/add_cartoon',methods=['POST'])
def add_cartoon():
    json_data=request.json
    try:
        data=cartoon_Schema.load(json_data)

        obj_collection.insert_one(data)

        return jsonify({"message":"Add successfully"}),201

    except ValidationError as er:
        return jsonify(er.messages),400
    
@main.route('/get_cartoon',methods=['GET'])
def get_cartoon():
    try:
        cartoon = obj_collection.find_one({}, {'_id': 0})

        if not cartoon:
            return jsonify({"error": "Cartoon not found"}),404
        
        return jsonify(cartoon_Schema.dump(cartoon)),200

    except Exception as e:
        return jsonify({"error": str(e)}),400





