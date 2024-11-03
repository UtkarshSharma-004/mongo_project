from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from config import setup_logging

logger = setup_logging

def get_db():

    uri = os.getenv('Mongo_URI')
    Client = MongoClient(uri,server_api=ServerApi('1'))

    db = Client ['COllection_database']

    check_connection(Client=Client)

    return db

def check_connection(Client):
    try:
        Client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to Mongo db!")
    except Exception as e:
        print(e)