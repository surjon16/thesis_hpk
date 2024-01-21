from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from application import app
from flask_httpauth import HTTPBasicAuth

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/db_hpk' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 300

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# WEB VIEWS WITH LOGIN REQUIRED
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = "strong"

# API BASIC AUTH
auth = HTTPBasicAuth()

csrf = CSRFProtect()
csrf.init_app(app)