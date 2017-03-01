from flask import render_template
from . import resort


@resort.route("")
def display_offers():
    return render_template('resort/resort.html')
