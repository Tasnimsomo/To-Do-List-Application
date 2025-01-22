from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.integer, primary_key=True)
    title = db.Colum(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    