import webbrowser

import random

import string



x = 0

mystring = ""

p = random.choice([5, 7])

while x < p:

    mystring = mystring + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    x = x + 1

myaddress = "http://imgur.com/gallery/" + mystring

webbrowser.open(myaddress)
