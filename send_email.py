from constants import username, password
from validate_email import validate_email
import sendgrid
import DNS

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
    message.set_text(email_text)
    #set the message from field
    message.set_from(from_email)
    #send the message
    #print "Sending the message to: "+user_email
    status, msg = sg.send(message)


def send_emails(to_emails,from_email,subject,msg):
    string_array = to_emails.split(',')
    for user_email in string_array:
        user_email = user_email.strip(' ')
        is_valid = validate_email(user_email)
        if is_valid:
            sendgrid_email(user_email,from_email,subject,msg)

