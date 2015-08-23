import requests

def chartbeat_request(api_key, host):
    api_call_url = (
        'http://api.chartbeat.com/live/toppages/?'
        'apikey=%s&host=%s&limit=100' % (api_key, host)
    )
    res = requests.get(api_call_url)
    return res

def process_data(data):
    result = {}
    for page in data:
        result[page['i']] = page['visitors'], page['path']
    return result
