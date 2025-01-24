from flask_sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    