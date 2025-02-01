from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
import os

load_dotenv('.env')
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

## Creating an engine to connect to the database related to the URL 
connection = create_engine(SQLALCHEMY_DATABASE_URL)

## creating tables based on the models stored in the Base.metadata
Base.metadata.create_all(connection)

## Creating a session to interact with the database
Session = sessionmaker(bind=connection)

session = Session()
