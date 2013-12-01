from flask import Flask, render_template, request
from hackathonlist import get_hackathons

#Instantiate flask object
app = Flask(__name__)

#Apply decorator to function with '@' where app.py resides
@app.route('/', methods=["get", "post"])
def index():
    hackathon_list = get_hackathons()
    #hackathon_list = hackathon_list is a keyword argument.
    return render_template("index.html", hackathon_list=hackathon_list)

@app.route('/search', methods=["post"])
def search():
    #request.form is a dictionary containing all of the post request form data
    date = request.form["query"]
    return date

app.run(host="0.0.0.0", port=5000)
