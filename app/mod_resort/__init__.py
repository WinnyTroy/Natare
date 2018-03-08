from flask import Blueprint


resort = Blueprint(name="resort", url_prefix="/about/", import_name=__name__)

from . import views
