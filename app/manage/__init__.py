from flask import Blueprint

manage = Blueprint('manage', __name__, url_prefix='/')

from app.manage import views
