import requests
import grequests
import random
import time
from user_agents import user_agents
from bs4 import BeautifulSoup


def build_city_urls(query):

    #list for all request urls
    url_list = []
    #random user agent taken from the list of user agents
    rand_user_agent = user_agents[random.randint(0,len(user_agents)-1)]
    user_agent = {'User-Agent': rand_user_agent}
    req = requests.get("http://geo.craigslist.org/iso/us/",headers=user_agent)
    html_text = req.text
    soup = BeautifulSoup(html_text)

    for child in soup.find_all(id='list'):
        for link in child.find_all('a'):
            search_link = link.get('href')+"search/sss?query="+query+"&sort=rel"
            url_list.append(search_link)
    req.close
    return url_list

#The div with the "content" class contains all of the results. Each "hdrlnk" class contains the
#description as well as the url, which is why it's convenient to use this class.

def get_results():

    #result paring
    result = {}

    url_list = build_city_urls()

    rand_user_agent = user_agents[random.randint(0,len(user_agents)-1)]
    user_agent = {'User-Agent': rand_user_agent}

    #sleep_time = random.random()
    #time.sleep(sleep_time)

    rs = (grequests.get(link,stream=False) for link in url_list)

    responses = grequests.map(rs,size=10)

    for req in responses:
        link = req.url.split('search')[0]
        #print "searching: "+link+"\nfor "+query+"."
        html_text = req.text
        soup = BeautifulSoup(html_text)
        for child in soup.find_all("div",class_="content"):
            for result_link in child.find_all("a",class_="hdrlnk"):
                #If a link exists  must check if the result is local to prepend the full link
                if "html" in result_link.get('href'):
                    if "http" not in result_link.get('href'):
                        full_link = link+result_link.get('href')
                    else:
                        full_link = result_link.get('href')

                    link_desc = result_link.get_text()
                    try:
                       link_desc.decode('ascii')
                    except UnicodeError:
                       link_desc = link_desc.encode('utf-8',"replace")
                    if not link_desc in result:
                       result[link_desc] = full_link
                       #print_result()
        req.close()
        return result

#Will include price later
#for result_link in child.find_all("a",class_="i"):
#get text from this child
