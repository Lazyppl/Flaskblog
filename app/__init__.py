from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()



app = Flask(__name__)
app.config.from_object('config')
login_manager.init_app(app)
bootstrap.init_app(app)
db = SQLAlchemy(app)
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
    
    

    