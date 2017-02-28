from flask import render_template
from . import offers


@offers.route("")
def display_offers():
    return render_template('generic.html')
