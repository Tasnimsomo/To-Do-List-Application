from Flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import session
from models import Task

app = Flask(__name__)
