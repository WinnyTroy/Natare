from flask import Blueprint

home = Blueprint('home', __name__, url_prefix='/')

from app.mod_home import views
