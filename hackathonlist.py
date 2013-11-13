import requests
import simplejson

def hackathon_list():
    hackathons = requests.get("http://hackerleague.org/api/v1/hackathons.json")
    hackathons = simplejson.loads(hackathons.text)

    hackathon_list = []
    for hackathon in hackathons:
       # print hackathon["name"]
      hackathon_list.append(hackathon["name"])

    return hackathon_list

print hackathon_list()
