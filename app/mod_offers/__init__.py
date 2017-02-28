from flask import Blueprint


offers = Blueprint(name="offers", url_prefix="/offers/", import_name=__name__)

from . import views
