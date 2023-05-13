import os

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Redis settings
    REDIS_HOST = os.environ.get('REDIS_HOST') or 'localhost' or '12345678'
    REDIS_PORT = int(os.environ.get('REDIS_PORT') or 6379)

    # MongoDB settings
    MONGODB_CONNECTION_STRING = os.environ.get('MONGODB_CONNECTION_STRING')