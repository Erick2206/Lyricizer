import urllib
import requests
from requests.auth import HTTPBasicAuth
import pprint
import json

# Bing API key
API_KEY = "GujotwKh+KtMj7xW0/nCwN62LRtgnTbfymhpRKJLWY0"

def bing_api(query, source_type = "Web", top = 5, format = 'json'):
    """Returns the decoded json response content

    :param query: query for search
    :param source_type: type for seacrh result
    :param top: number of search result
    :param format: format of search result
    """

    API_KEY = "GujotwKh+KtMj7xW0/nCwN62LRtgnTbfymhpRKJLWY0"

    # set search url
    query = '%27' + urllib.quote(query) + '%27'
    # web result only base url
    base_url = 'https://api.datamarket.azure.com/Bing/Search/v1/Web'
    url = base_url + '?Query=' + query + '&$top=' + str(top) + '&$format=' + format

    # create credential for authentication
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    # create auth object
    auth = HTTPBasicAuth("", API_KEY)
    # set headers
    headers = {'User-Agent': user_agent}

    # get response from search url
    response_data = requests.get(url, auth = auth)
    # decode json response content
    json_result = response_data.json()
    # decode json response content  json.loads(r.text)
    json_result = response_data.json()
#    json_result = json.loads(str(response_data))
    return json_result

if __name__=="__main__":
    pprint.pprint(bing_api("jack u take u there az lyrics"))
