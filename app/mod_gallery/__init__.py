from flask import Blueprint


gallery = Blueprint(name="gallery", url_prefix="/gallery/", import_name=__name__)

from . import views
