
from smtplib import SMTP
from smtplib import SMTPException
from email.mime.text import MIMEText
from emails import email_text,subject,from_email
from constants import gmail_password
import sys
 
#Global varialbes
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587
TEXT_SUBTYPE = "plain"
 
def send_email(recipient):
     
    #Create the message
    msg = MIMEText(email_text, TEXT_SUBTYPE)
    msg["Subject"] = subject 
    msg["From"] = from_email 
    msg["To"] = recipient 
     
    try:
      smtpObj = SMTP(GMAIL_SMTP, GMAIL_SMTP_PORT)
      #Identify yourself to GMAIL ESMTP server.
      smtpObj.ehlo()
      #Put SMTP connection in TLS mode and call ehlo again.
      smtpObj.starttls()
      smtpObj.ehlo()
      #Login to service
      smtpObj.login(user=from_email, gmail_password)
      #Send email
      smtpObj.sendmail(from_email, recipient.split(), msg.as_string())
      #close connection and session.
      smtpObj.quit();
    except SMTPException as error:
      print "Error: unable to send email :  {err}".format(err=error)

def send_emails():
    text_file = raw_input("Enter the name of the text file")
    with open(text_file, 'r') as f:
        for user_email in f:
            send_email(user_email)

send_emails()
