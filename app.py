from flask import Flask, request, jsonify
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
        'message': 'Task added successfully'
    }), 201

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    tasks = session.query(Task).all()

    task_list = [
        {
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "created_at": task.created_at
        }
        for task in tasks
    ]

    return jsonify({
        "tasks": task_list
    }), 200






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
