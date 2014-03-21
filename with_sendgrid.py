from constants import username, password
from validate_email import validate_email
from emails import email_text, subject, from_email 
import sendgrid
import DNS
import re


def sendgrid_email(user_email):
    #Securely connect to SendGrid
    sg = sendgrid.SendGridClient(username, password, secure=True)
    #Make Empty Message
    message = sendgrid.Mail()
    #attach a file
    message.add_attachment_stream('Resume_Tobias_Perelstein.pdf','Resume')
    #Add recipient
    message.add_to(user_email)
    #set the subject of the email
    message.set_subject(subject)
    #set the body of the message
    message.set_text(email_text)
    #set the message from field
    message.set_from(from_email)
    #send the message
    status, msg = sg.send(message)

#This function takes a tab or comma delimited file and parses the file for all valid emails. 
def send_emails():
    text_file = raw_input("Enter the name of the text file\n")
    with open(text_file, 'r') as f:
        for line in f:
            string_array = re.split('\t|,',line)
            for user_email in string_array:
                user_email = user_email.strip(' ')
                is_valid = validate_email(user_email)
                if is_valid:
                    sendgrid_email(user_email)

send_emails()
