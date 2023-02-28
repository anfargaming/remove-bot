import os
from pymongo import MongoClient

class Database:
    def __init__(self, url):
        self.client = MongoClient(url)
        self.db = self.client.get_database()
        self.users_collection = self.db.get_collection('users')

    def add_user(self, user_id, user_name):
        user = {'_id': user_id, 'name': user_name}
        result = self.users_collection.insert_one(user)
        return result.inserted_id

    def get_user(self, user_id):
        user = self.users_collection.find_one({'_id': user_id})
        return user

    def remove_user(self, user_id):
        result = self.users_collection.delete_one({'_id': user_id})
        return result.deleted_count
