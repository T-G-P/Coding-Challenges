from validate_email import validate_email
from smtplib import SMTP
from smtplib import SMTPException
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from emails import email_text, subject, from_email
from constants import gmail_password
import sys
import DNS
import re

#Global varialbes
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587
TEXT_SUBTYPE = "plain"
 
#This function takes in a recipient and sends them an email
def send_email(recipient):
     
    #Create the message
    msg = MIMEMultipart()
    #msg = MIMEText(email_text, TEXT_SUBTYPE)
    msg["Subject"] = subject 
    msg["From"] = from_email 
    msg["To"] = recipient 

    part = MIMEText(email_text, TEXT_SUBTYPE)
    msg.attach(part)
    part = MIMEApplication(open("Resume_Tobias_Perelstein.pdf","rb").read())
    part.add_header('Content-Disposition', 'attachment', filename="Resume_Tobias_Perelstein.pdf")
    msg.attach(part)
     
    try:
      smtpObj = SMTP(GMAIL_SMTP, GMAIL_SMTP_PORT)
      #Identify yourself to GMAIL ESMTP server.
      smtpObj.ehlo()
      #Put SMTP connection in TLS mode and call ehlo again.
      smtpObj.starttls()
      smtpObj.ehlo()
      #Login to service
      smtpObj.login(user=from_email, password=gmail_password)
      #Send email
      smtpObj.sendmail(from_email, recipient.split(), msg.as_string())
      #close connection and session.
      smtpObj.quit();
    except SMTPException as error:
      print "Error: unable to send email :  {err}".format(err=error)

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
                    send_email(user_email)

send_emails()
