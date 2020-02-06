from flask import Flask
from socialPlaylist.forms import RegForm, LoginForm
import secrets
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


application = app

# Placed below to avoid circular import of app
from socialPlaylist import routes, models