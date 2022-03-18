from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'key'
db = SQLAlchemy(app)

from app import routes, models
app.run(debug=True)


