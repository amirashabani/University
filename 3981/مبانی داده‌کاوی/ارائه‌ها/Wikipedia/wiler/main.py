import category, json, sys

category_name = "Computer science"

category_dict = {
    "name": category_name,
    "categories": [],
    "pages": []
}

colors = {
    "green": "\033[92m",
    "blue": "\033[94m",
    "reset": "\x1b[0m"
}

def parse(dict, name, indent=0):
    print(f'{" "*indent}{name}')
    for page in category.get_pages(name):
        if(page[:9] == "Category:"):
            cat_name = page.replace("Category:", "")
            dict["categories"].append({
                "name": cat_name,
                "categories": [],
                "pages": []
            })
            sys.stdout.write('\033[2K')
            print(f'{colors["green"]}{" "*(indent+1)}{cat_name}{colors["reset"]}', end='\r')
        else:
            cat_list = category.get_categories(page)
            dict["pages"].append({
                "name": page,
                "categories": cat_list
            })
            sys.stdout.write('\033[2K')
            print(f'{colors["blue"]}{" "*(indent+1)}{page}{colors["reset"]}', end='\r')

parse(category_dict, category_name)
parse(category_dict["categories"][0], "Areas of computer science", 1)

with open(f'{category_name}.json', 'w') as file:
    file.write(json.dumps(category_dict))
