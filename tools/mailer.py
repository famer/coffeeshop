from flask import Flask, render_template, current_app
from flask.ext.mail import Mail, Message
from tools.js import json_loader
import os

app = Flask(__name__)
#app.config.from_object('config')
mail = Mail(app)
app = current_app


def send_email(subject, sender, recipients, data):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = render_template('emails/txt/order_admin.txt',
    							 form=data,
    							 ordered=enumerate(data.getlist('esig')),
    							 esigs=json_loader(os.path.join(app.root_path, app.config['ESIGS_JSON']))).encode("UTF-8")
    msg.html = render_template('emails/order_admin.html',
    							 form=data,
    							 ordered=enumerate(data.getlist('esig')),
    							 esigs=json_loader(os.path.join(app.root_path, app.config['ESIGS_JSON']))).encode("UTF-8")

    mail.send(msg)


def send_mail(data):
	import smtplib
	msg = render_template('emails/order_admin.html', form=data).encode("UTF-8")

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('dj.famer@gmail.com','')
	server.sendmail('dj.famer@gmail.com','djfamer@gmail.com',msg)
	server.close()
