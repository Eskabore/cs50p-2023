import sys
from redis import Redis
from pymongo import MongoClient
from bson.objectid import ObjectId
from app import app

# Redis connection
redis_conn = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
print(redis_conn.ping())

# Check Redis connection
try:
    redis_conn.ping()
    print("Successfully connected to Redis.")
except Exception as e:
    print("Error connecting to Redis: ", e, file=sys.stderr)
    sys.exit(1)



# MongoDB connection
client = MongoClient(app.config['MONGODB_CONNECTION_STRING'])
print(client.server_info())
db = client['task_queue']
tasks_collection = db['tasks']