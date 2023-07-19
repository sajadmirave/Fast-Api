from pymongo import MongoClient


def connection():
    # connect 
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
