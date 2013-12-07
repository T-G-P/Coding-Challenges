import requests
import simplejson

def get_hackathons():
    hackathons = requests.get("http://hackerleague.org/api/v1/hackathons.json")

    #takes json text and loads json object
    hackathons = simplejson.loads(hackathons.text)
    for hackathon in hackathons:
        print hackathon["name"] + " " +  hackathon["start_time"] + " " + hackathon["end_time"]

    hackathon_dict = {}
    for hackathon in hackathons:
      hackathon_dict[hackathon["name"]] = hackathon["url"]

    return hackathon_dict

get_hackathons()
