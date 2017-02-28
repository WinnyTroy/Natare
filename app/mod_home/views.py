from . import home
from controller import Functionality
from app.forms import ContactForm
from flask import render_template, url_for, redirect, request


@home.route("/")
@home.route("index")
@home.route("home")
def index():
    return render_template('home/index.html')


@home.route("menu")
def display_menu():
    return render_template('menu/elements.html')


@home.route("reservation", methods=['POST', 'GET'])
def display_reservation():
    contact_form = ContactForm()

    if request.method == "GET":
        return render_template('reserve.html')
    elif request.method == "POST":

        # store data input by the users into their various db fields.
        # allocate the paths to be more precise
        first = request.form["firstName"]
        middle = request.form["MiddleName"]
        last = request.form["lastName"]
        work = request.form["occupation"]
        email = request.form["email"]
        arrival = request.form["arrivalDate"]
        departure = request.form["departureDate"]

        Functionality.db_access(first, middle, last,
                                work, email, arrival, departure)
        Functionality.generate_pdf(first, middle, last)
        return redirect(url_for('mod_home.index'))

    return render_template('index.html')
