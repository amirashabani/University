import category, requests, csv
from urllib.parse import unquote

random_url = "https://en.wikipedia.org/wiki/Special:Random"

def fetch():
    title = ''
    with open('rawi.csv', 'a') as rawi_file:
        writer = csv.writer(rawi_file)
        r = requests.get(random_url)
        url = r.url
        title = unquote(url.split('/')[-1]) # extract what comes after the last backslash, thus the title

        categories = category.get_categories(title)

        row = []
        row.append(title)
        row.extend(categories)
        writer.writerow(row)
    
    return title

def count_rows():
    with open('rawi.csv', 'r') as rawi_file:
        reader = csv.reader(rawi_file, delimiter=',')
        data = list(reader)
        return len(data)
