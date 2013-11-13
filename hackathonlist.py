import requests
import simplejson

hackathons = requests.get("http://hackerleague.org/api/v1/hackathons.json")
hackathons = simplejson.loads(hackathons.text)

for hackathon in hackathons:
    print hackathon["name"]
