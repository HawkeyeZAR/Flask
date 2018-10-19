from flask import Flask, render_template, request, flash
from contactpage.forms import ContactForm
from contactpage.config import Config
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(Config)   # get secret key from config

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": '',
    "MAIL_PASSWORD": ''
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', title='Contact', form=form)
        else:
            msg = Message(form.subject.data, sender=form.email.data, recipients=['jack.ackermann@gmail.com'])
            msg.body = "From: {0} - <{1}> \n{2}".format(form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', title='Contact', form=form)



if __name__ == '__main__':
    app.run()
