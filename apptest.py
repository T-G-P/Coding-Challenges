from flask import Flask, render_template, request
from constants import username, password
from validate_email import validate_email
import sendgrid
import urllib2
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    from_email = request.form['from_email']
    to_emails = request.form['to_email']
    subject = request.form['subject']
    msg = request.form['msg']

    def sendgrid_email(user_email):
        #Securely connect to SendGrid
        sg = sendgrid.SendGridClient(username, password, secure=True)
        #Make Empty Message
        message = sendgrid.Mail()
        #Add recipient
        message.add_to(user_email)
        #set the subject of the email
        message.set_subject(subject)
        #set the body of the message
        message.set_text(msg)
        #set the message from field
        message.set_from(from_email)
        #send the message
        status, msg = sg.send(message)

    def send_emails():
        string_array = to_emails.split(',')
        for user_email in string_array:
            user_email = user_email.strip(' ')
            is_valid = validate_email(user_email)
            if is_valid:
                sendgrid_email(user_email)

        
    send_emails()
    return render_template('result.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)
