import os
from pymongo import MongoClient

class Database:
    def __init__(self, mongo_url, db_name):
        self.client = MongoClient(mongo_url)
        self.db = self.client.get_database(db_name)
        self.users_collection = self.db.get_collection('users')

def add_user(user_id, user_name):
    user = {'_id': user_id, 'name': user_name}
    result = Database.users_collection.insert_one(user)
    return result.inserted_id


def get_user(user_id):
    user = Database.users_collection.find_one({'_id': user_id})
    return user


def remove_user(user_id):
    result = Database.users_collection.delete_one({'_id': user_id})
    return result.deleted_count
