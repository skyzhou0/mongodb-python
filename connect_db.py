import pymongo

DB_NAME = "contracts"


def get_database_connection():
    """
    this function should create a connection with MongoClient and return a
    database object
    """
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')

    return client[DB_NAME]