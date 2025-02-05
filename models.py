from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# this creates a base class that allows sqlalchemy to automatically map classes to tables
Base = declarative_base()
db = SQLAlchemy()

# class Task inherits from Base to create a table named tasks
class Task(Base):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    