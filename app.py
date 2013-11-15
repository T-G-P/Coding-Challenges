from flask import Flask
from hackathonlist import get_hackathons
#Instantiate flask object
app = Flask(__name__)

#Apply decorator to function with '@' where app.py resides
@app.route('/', methods=["get", "post"])


def index():
    hackathon_list = ""

    for hackathon in get_hackathons():
        hackathon_list+=hackathon+'\n'+'<br>'
    return hackathon_list

app.run(host="0.0.0.0", port=5000)
