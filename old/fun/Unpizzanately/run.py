from flask import Flask, request, render_template
from twilio.util import TwilioCapability
from twilio.rest import TwilioRestClient
import twilio.twiml

import re

app = Flask(__name__)

account_sid = "AC9c5adc79b9cf3d79fc46f47fa6165c1e"
auth_token = "6c79f8833d77a2a0433db0418d33d0c7"
application_sid = "APaa7ff4fb5efb45971236e6762e90b1ba" # Twilio Application Sid

# Add a Twilio phone number or number verified with Twilio as the caller ID
caller_id = "+19088450320"

# put your default Twilio Client name here, for when a phone number isn't given
default_client = "tobias"

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    #dest_number = request.values.get('PhoneNumber', None)
    dest_number = '+17328750553'
    resp = twilio.twiml.Response()

    with resp.dial(callerId=caller_id) as r:
    # If we have a number, and it looks like a phone number:
        if dest_number and re.search('^[\d\(\)\- \+]+$', dest_number):
            r.number(dest_number)
            name = "tobias"
            conference()
            url = "tobias.ngrok.com/conference/"+name
            call_pizza(url)
    print dest_number

    return str(resp)

@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""

    capability = TwilioCapability(account_sid, auth_token)
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming("tobias")
    token = capability.generate()

    return render_template('client.html', token=token)

@app.route('/conference/<username>', methods=['GET','POST'])
def conference():
    #username = request.values.get('name', None)
    r = twilio.twiml.Response()
    r.say("Hello "+username)
    return str(r)

def call_pizza(url):
    client = TwilioRestClient(account_sid, auth_token)
    call = client.calls.create(url,
            #to="+19082274177",
            to=request.values.get('PhoneNumber', None),
            from_="+17328750553")
    print call.sid


if __name__ == "__main__":
    app.run(debug=True)
