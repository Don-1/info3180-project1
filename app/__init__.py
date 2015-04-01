from flask import Flask
<<<<<<< HEAD
from config import SQLALCHEMY_DATABASE_URI
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views

=======
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'
app.config['CSRF_ENABLED'] = False
db = SQLAlchemy(app)

from app import views, models
>>>>>>> 220afe0f976d85dc7a46f7cc89eb3ca0a859900f
