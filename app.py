from flask import Flask, render_template, request
from constants import username, password
import requests
import urllib2
import os
import with_sendgrid

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
    send_emails(to_emails,from_email,subject,msg);
    return render_template('results.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)
