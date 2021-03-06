from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(FlaskForm):
	name = TextField("Name", [validators.Required("Please enter your name.")])
	email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	subject = TextField("Subject", [validators.Required("Please enter a subject.")])
	message = TextAreaField("Your Message", [validators.Required("Please enter a message.")])
	submit = SubmitField("Send Message")
