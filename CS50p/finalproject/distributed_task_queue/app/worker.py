import time
import random
from app.database import tasks_collection
from pymongo import MongoClient, ReturnDocument

# Function stimulates task processing and update task status in MongoDB
def perform_task(task_id, data):
    # Simulate task processing time
    processing_time = random.randint(1, 10)
    time.sleep(processing_time)

    # Update task status and result in MongoDB
    result = "Task completed in {} seconds.".format(processing_time)
    tasks_collection.find_one_and_update(
        {'_id': MongoClient().task_queue.tasks_collection.ObjectId(task_id)},
        {'$set': {'status': 'completed', 'result': result}},
        return_document=ReturnDocument.AFTER
    )
