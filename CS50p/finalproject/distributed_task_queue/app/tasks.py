import pymongo
from app import app
from flask import request, jsonify
import sys
from app.database import tasks_collection, redis_conn
from app.worker import perform_task
from rq import Queue
from bson import ObjectId
from datetime import datetime


# RQ queues
low_priority_queue = Queue('low', connection=redis_conn)
medium_priority_queue = Queue('medium', connection=redis_conn)
high_priority_queue = Queue('high', connection=redis_conn)

# Check RQ queue connection
try:
    queue_length = low_priority_queue.count  # Updated to use low_priority_queue instead of queue
    print(f"Successfully connected to RQ queue. Current queue length: {queue_length}")
except Exception as e:
    print("Error connecting to RQ queue: ", e, file=sys.stderr)
    sys.exit(1)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Distributed Task Queue API!"

# Function to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if request.content_type != 'application/json':
        return 'request Content-Type was not "application/json".', 415

    data = request.get_json()

    # Add 'created_at' field with the current timestamp
    data['created_at'] = datetime.utcnow()

    # Add 'status' field with the default value 'pending'
    data['status'] = 'pending'

    task_id = tasks_collection.insert_one(data).inserted_id

    # Determine target queue based on priority
    priority = data.get('priority', 'low')
    if priority == 'high':
        target_queue = high_priority_queue
    elif priority == 'medium':
        target_queue = medium_priority_queue
    else:
        target_queue = low_priority_queue

    job = target_queue.enqueue_call(
        perform_task,
        args=(str(task_id), data),
        result_ttl=86400
    )
    return jsonify({'task_id': str(task_id), 'job_id': job.id}), 201

# Function to get the status and result of a task
@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})
    if task:
        response = {
            'task_id': str(task['_id']),
            'status': task.get('status'),
            'result': task.get('result', None)
        }
        return jsonify(response)
    else:
        return jsonify({'error': 'Task not found'}), 404


# Route for monitoring task status
@app.route('/tasks/<job_id>/status', methods=['GET'])
def get_task_status(job_id):
    job = None
    for queue in [high_priority_queue, medium_priority_queue, low_priority_queue]:
        job = queue.fetch_job(job_id)
        if job:
            break

    if not job:
        return jsonify({'error': 'Job not found'}), 404

    return jsonify({'status': job.get_status()}), 200


# Function to update the status of a task
@app.route('/tasks/<task_id>/status', methods=['PUT'])
def update_task_status(task_id):
    if request.content_type != 'application/json':
        return 'request Content-Type was not "application/json".', 415

    data = request.get_json()
    new_status = data.get('status', None)
    new_result = data.get('result', None)  # Get the result from the request data
    if new_status:
        update_data = {'status': new_status}
        if new_result:
            update_data['result'] = new_result  # Add the result to the update data if it's not None

        tasks_collection.update_one(
            {'_id': ObjectId(task_id)},
            {'$set': update_data}
        )
        return jsonify({'message': 'Task status updated'}), 200
    else:
        return jsonify({'error': 'Invalid status'}), 400


@app.route('/tasks/<task_id>/details', methods=['GET'])
def get_task_details(task_id):
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})
    if task:
        response = {
            'task_id': str(task['_id']),
            'description': task['description'],
            'priority': task['priority'],
            'created_at': task.get('created_at', None),  # Use get() to avoid KeyError
            'status': task.get('status', None)  # Use get() to avoid KeyError
        }
        return jsonify(response), 200
    else:
        return jsonify({'error': 'Task not found'}), 404



# Function to retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    # Get query parameters for pagination, sorting, and filtering
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    sort_by = request.args.get('sort_by', 'created_at')
    sort_order = request.args.get('sort_order', 'asc')
    priority = request.args.get('priority', None)
    status = request.args.get('status', None)

    # Build filter query based on priority and status
    filter_query = {}
    if priority:
        filter_query['priority'] = priority
    if status:
        filter_query['status'] = status

    # Build sort query based on sort_by and sort_order
    sort_query = [(sort_by, pymongo.ASCENDING if sort_order == 'asc' else pymongo.DESCENDING)]

    # Retrieve tasks from collection using find(), skip(), limit(), and sort()
    tasks = tasks_collection.find(filter_query).skip((page - 1) * per_page).limit(per_page).sort(sort_query)

    # Convert tasks to JSON format
    response = []
    for task in tasks:
        response.append({
            'task_id': str(task['_id']),
            'description': task.get('description'),
            'priority': task.get('priority'),
            'created_at': task.get('created_at', None),  # Use get() to avoid KeyError
            'status': task.get('status', 'unknown'),
            'result': task.get('result', None)  # Use get() for the 'result' field as well
        })

    return jsonify(response), 200


# Function to delete a task by ID
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})
    if task:
        tasks_collection.delete_one({'_id': ObjectId(task_id)})

        # Get the job_id from the task document
        job_id = task.get('job_id', None)  # Use get() to avoid KeyError

        # Cancel the corresponding job in the task queue
        if job_id:
            for queue in [low_priority_queue, medium_priority_queue, high_priority_queue]:
                job = queue.fetch_job(job_id)
                if job:
                    job.cancel()
                    break

        return jsonify({'message': 'Task deleted'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404
