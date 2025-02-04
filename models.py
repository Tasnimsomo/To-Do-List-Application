from flask_sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

# this creates a base class that allows sqlalchemy to automatically map classes to tables
Base = declarative_base()

# class Task inherits from Base to create a table named tasks
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(datetime, default=datetime.now)

    