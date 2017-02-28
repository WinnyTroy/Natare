import pdfkit
from flask import render_template, make_response
import smtplib


def generate_pdf(name):
    rendered = render_template('reserve.html', name=name)
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename = bookings.pdf'


def send_email(message, to):
    # setting up the smtp server details to use
    server = smtplib.SMTP('smtp.gmail.com:587')

    server.ehlo()

    server.starttls()

    server.login('nataregarz@gmail.com', 'natar312')

    server.sendmail(to_addrs=to, from_addr='kiraguwinnie@gmail.com', msg=message)

    server.close()
