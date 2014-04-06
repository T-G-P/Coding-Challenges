from flask import Flask, render_template, request
from send_email import send_emails
import urllib2
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    to_emails = request.form['to_email']
    from_email = request.form['from_email']
    subject = request.form['subject']
    msg = request.form['msg']
    send_emails(to_emails, from_email, subject, msg)
    return render_template('result.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port, debug='true')
