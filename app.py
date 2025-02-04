from flask import Flask, request, jsonify
from models import Task
from database import session

app = Flask(__name__)


@app.route('/add_tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    if not title:
        return jsonify({'message': 'Title is required'}), 400
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()
    return jsonify({
        'message': 'Task added successfully',
        'title': title,
        'description': description,
    }), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
