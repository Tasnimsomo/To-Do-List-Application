from flask import Flask, request, jsonify, json
from models import Task
from database import session
from datetime import datetime

app = Flask(__name__)


@app.route('/add_tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed', False);
    created_at = datetime.now()
    if not title:
        return jsonify({'message': 'Title is required'}), 400
    new_task = Task(title=title, description=description, completed=completed, created_at=created_at)
    session.add(new_task)
    session.commit()
    return jsonify({
        'title': title,
        'description': description,
        'completed': completed,
        'created_at': created_at,
        'id': new_task.id,
        'message': 'Task added successfully'
    }), 201

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    tasks = session.query(Task).all()
    task_list = [
        {
            "title": task.title,
            "description": task.description if isinstance(task.description, dict) else json.loads(task.description),
            "completed": task.completed,
            "id": task.id,
            "created_at": task.created_at
        }
        for task in tasks
    ]

    return jsonify({
        "tasks": task_list
    }), 200

## remove by id
@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        return jsonify({
            'message': 'Task not found'
        }), 404
    session.delete(task)
    session.commit()
    return jsonify({
        'message': f"Task {task.title} deleted successfully"
    }), 200


@app.route('/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = session.query(Task).filter_by(Task.id == task_id).first()
    if not task:
        return jsonify({
            'message': "Task not found"
        }), 404

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')
    if title:
        task.title = title
    if description:
        task.description = description
    if completed:
        task.completed = completed
    session.commit()
    return jsonify({
        'message': 'Task updated successfully'
    }), 200
    

# toggle task by id from complete to incomplete and vice versa
@app.route('/toggle_task/<int:task_id>', methods=['PATCH'])
def toggle_task(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        return jsonify({
            'message': "Task not found"
        }), 404
    task.completed = not task.completed
    session.commit()
    return jsonify({
        'message': f'Task {task.title} toggled successfully'
    }), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
