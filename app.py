from Flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import session
from models import Task

app = Flask(__name__)

@app.route('/')
def index():
    tasks = session.query(Task).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = Task(title=request.form['title'])
    session.add(task)
    session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    task = session.query(Task).filter_by(id=id).first()
    session.delete(task)
    session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
