import os


class Config(object):
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    MONGODB_URI = os.environ.get('MONGODB_URI')
