from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db17c914b0e06f3eb272687c260bcb07' # To stop some kind of cookie manipulation?
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Function name of login route
login_manager.login_message_category = 'info' # Bootstrap Info class

from flaskblog import routes
