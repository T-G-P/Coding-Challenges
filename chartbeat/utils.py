import requests
import requests_cache

# Looking at the chartbeat api headers, the rate limit of 200req/min, so
# 3.33req/second. Set the cache to persist for 3 seconds
requests_cache.install_cache('chartbeat_cache',
                             backend='redis',
                             expire_after=3)


def chartbeat_request(api_key, host):
    """
    return a requests object. Using the open source
    requests_cache library which caches the request and
    attaches a True/False 'from_cache' property to the request
    """

    api_call_url = ('http://api.chartbeat.com/live/toppages/?'
                    'apikey=%s&host=%s&limit=100' % (api_key, host))
    return requests.get(api_call_url)


def convert_data(data):
    """
    Process  and convert the json response from the api
    so that it can be quickly iterated through and visitor
    count can be retrieved linearly
    """

    result = {}
    for page in data:
        result[page['i']] = page['visitors'], page['path']

    return result
