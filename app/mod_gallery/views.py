from flask import render_template
from . import gallery


@gallery.route("")
def display_gallery():
    return render_template('gallery.html')
