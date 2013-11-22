import requests
import simplejson

def get_hackathons():
    hackathons = requests.get("http://hackerleague.org/api/v1/hackathons.json")
    hackathons = simplejson.loads(hackathons.text)

    hackathon_dict = {}
    for hackathon in hackathons:
      hackathon_dict[hackathon["name"]] = hackathon["url"]

    return hackathon_dict

