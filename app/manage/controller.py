import pdfkit
from flask import render_template, request, make_response
from app.models import Users, Booking
from app import db
import smtplib


class Functionality(object):
    @staticmethod
    def db_access(first, middle, last, work, email, arrival, departure):
        """
        # Now setup an instance of the tables we are going 
        to interact with in order to store data
        # instantiate the variables just declared up there with 
        the relevant field in the table that the data will go to
        # giving it a path

        :param first:
        :param middle:
        :param last:
        :param work:
        :param email:
        :return:
        """
        email_string = "Hello, " + first + middle + last + \
                       " you have made a reservation for " + arrival + " to " + departure
        clients = Users(f_name=first, m_name=middle, l_name=last,
                        occupation=work, email_address=email)

        duration = Booking(arrival_date=arrival, departure_date=departure)
        Functionality.send_email(email_string, email)

        # then add these new stored infor to the current user session
        # commit the changes
        db.session.add(clients)
        db.session.add(duration)
        db.session.commit()

    @staticmethod
    def generate_pdf(first, middle, last):
        rendered = render_template('reserve.html', first=request.form["firstName"],
                                   middle=request.form["MiddleName"],
                                   last=request.form["lastName"])
        pdf = pdfkit.from_string(rendered, False)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers[
            'Content-Disposition'] = 'inline; filename = bookings.pdf'

        return response

    @staticmethod
    def send_email(response, receiver):
        # setting up the smtp server details to use
        server = smtplib.SMTP('smtp.gmail.com:587')

        server.ehlo()

        server.starttls()

        server.login('nataregarz@gmail.com', 'natar312')

        server.sendmail(to_addrs=receiver,
                        from_addr='kiraguwinnie@gmail.com', msg=response)

        server.close()
