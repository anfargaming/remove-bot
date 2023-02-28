import os
from pymongo import MongoClient

class Database:
    def __init__(self, mongo_url, db_name):
        self.client = MongoClient(mongo_url)
        self.db = self.client.get_database(db_name)
        self.users_collection = self.db.get_collection('users')

MONGODB_URL = os.environ.get('MONGODB_URL')
if not MONGODB_URL:
    raise ValueError('MONGODB_URL environment variable not set')

DB_NAME = "Cluster0"
db = Database(MONGODB_URL, DB_NAME)

def add_user(user_id, user_name):
    user = {'_id': user_id, 'name': user_name}
    result = db.users_collection.insert_one(user)
    return result.inserted_id


def get_user(user_id):
    user = db.users_collection.find_one({'_id': user_id})
    return user


def remove_user(user_id):
    result = db.users_collection.delete_one({'_id': user_id})
    return result.deleted_count
