from flask import Flask

#Instantiate flask object
app = Flask(__name__)

#Apply decorator to function with '@' where app.py resides
@app.route('/', methods=["get", "post"])
def index():
    return "Hello World"

app.run(host="0.0.0.0", port=5000)
