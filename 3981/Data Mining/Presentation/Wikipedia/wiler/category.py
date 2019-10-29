import requests
from time import sleep

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

    sleep(1)
    request = session.get(url=url, params=params)
    data = request.json()

    pageid = list(data['query']['pages'])[0]

    for category in data['query']['pages'][pageid]['categories']:
        categories.append(category['title'].replace('Category:', ''))

    return categories

def get_pages(category):
    pages = []
    session = requests.Session()

    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": f'Category:{category}',
        "cmlimit": "max",
        "format": "json"
    }

    sleep(1)
    request = session.get(url=url, params=params)
    data = request.json()

    for page in data['query']['categorymembers']:
        pages.append(page['title'])

    return pages
