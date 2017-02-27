from flask import Flask
from app.manage.views import manage
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(manage)

