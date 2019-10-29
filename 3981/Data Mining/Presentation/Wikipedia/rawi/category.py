import requests
from time import sleep

sleep_duration = 3 # seconds

url = "https://en.wikipedia.org/w/api.php"

def get_categories(title):
    categories = []
    session = requests.Session()

    params = {
        "action": "query",
        "prop": "categories",
        "titles": title,
        "clshow": "!hidden",
        "cllimit": "500",
        "format": "json"
    }

    sleep(sleep_duration)
    request = session.get(url=url, params=params)
    data = request.json()

    pageid = list(data['query']['pages'])[0]

    for category in data['query']['pages'][pageid]['categories']:
        categories.append(category['title'].replace('Category:', ''))

    return categories