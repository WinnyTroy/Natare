from . import home
from app.mod_home.controller import generate_pdf, send_email
from app.forms import ContactForm
from flask import render_template, url_for, redirect, request
from app import db
from app.models import Users, Booking


@home.route("/")
@home.route("index")
@home.route("home", methods=['POST', 'GET'])
def index():
    contact_form = ContactForm(request.form)

    if request.method == "POST":
        if contact_form.validate_on_submit():
            name = contact_form.name.data
            email = contact_form.email.data
            arrival = contact_form.arrival_date.data
            departure = contact_form.departure_date.data

            user = Users(f_name=name, m_name="middle", l_name="last",
                         occupation="work", email_address=email)

            duration = Booking(arrival_date=arrival, departure_date=departure)

            db.session.add(user)
            db.session.add(duration)
            db.session.commit()

            email_string = "Hello, " + name + \
                           " you have made a reservation for " + arrival + " to " + departure
            send_email(email_string, email)
            generate_pdf(name)

        return redirect(url_for('home.index'))

    return render_template('home/index.html', contact_form=contact_form)


@home.route("parishes")
def display_menu():
    return render_template('menu/elements.html')
