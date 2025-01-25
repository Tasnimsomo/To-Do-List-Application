from Flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import session
from models import Task

app = Flask(__name__)


# route for listing all tasks
@app.route('/', methods=['GET'])
def index():
    tasks = session.query(Task).all()
    return render_template('index.html', tasks=tasks)

# route for adding a new task
@app.route('/add', methods=['POST'])
def add():
    task = Task(title=request.form['title'])
    session.add(task)
    session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    task = session.query(Task).filter_by(id=id).first()
    session.delete(task)
    session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    task = session.query(Task).filter_by(id=id).first()
    task.title = request.form['title']
    session.commit()
    return redirect(url_for('index'))

@app.route('/complete_task/<int:id>', methods=['POST'])
def complete_task(id):
    task = session.query(Task).filter_by(id=id).first()
    task.completed = True
    session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete_task/<int:id>', methods=['POST'])
def incomplete_task(id):
    task = session.query(Task).filter_by(id=id).first()
    task.completed = False
    session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
