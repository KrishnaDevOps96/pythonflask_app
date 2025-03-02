from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task list
TASKS = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Deploy to Cloud Run", "done": False}
]

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(TASKS)

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or not 'title' in data:
        return jsonify({'error': 'Title is required'}), 400

    new_task = {
        "id": len(TASKS) + 1,
        "title": data['title'],
        "done": data.get('done', False)
    }
    TASKS.append(new_task)
    return jsonify(new_task), 201

# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in TASKS if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    task.update({
        'title': data.get('title', task['title']),
        'done': data.get('done', task['done'])
    })
    return jsonify(task)

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global TASKS
    TASKS = [task for task in TASKS if task['id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
