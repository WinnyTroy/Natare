from flask import Blueprint


resort = Blueprint(name="resort", url_prefix="/resort/", import_name=__name__)

from . import views
