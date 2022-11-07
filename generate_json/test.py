import json
from random import *
from function import generate_list_from_txt

# ------------------- les list -------------------
name = generate_list_from_txt()
# create a list with 30 countries 
country_names = [ 'France', 'Germany', 'Italy', 'Spain', 'Portugal', 'Belgium', 'Netherlands', 'Luxembourg', 'Switzerland', 'Austria', 'Poland', 'Czech Republic', 'Slovakia', 'Hungary', 'Romania', 'Bulgaria', 'Greece', 'Turkey', 'Bosnia and Herzegovina', 'Serbia', 'Montenegro', 'Macedonia', 'Albania', 'Croatia', 'Slovenia', 'Moldova', 'Ukraine', 'Belarus', 'Russia', 'Kazakhstan', 'China', 'Japan', 'South Korea', 'North Korea', 'Vietnam', 'Thailand', 'Laos', 'Cambodia', 'Myanmar', 'Malaysia', 'Indonesia', 'Philippines', 'Singapore', 'Brunei', 'Australia', 'New Zealand', 'India', 'Pakistan', 'Afghanistan', 'Iran', 'Iraq', 'Saudi Arabia', 'Yemen', 'Oman', 'United Arab Emirates', 'Qatar', 'Bahrain', 'Kuwait']

# ------------------- generate json -------------------
# creation a fucntion that generate and save data to json file, random choice in list names and country_names
def generate_json():
# create a list of 100 pepole
    data = []
    for i in range(100):
        data.append({
            'id': i,
            'name': choice(list(name)),
            'country': choice(list(country_names)),
            'age': randint(18, 65),
            'salary': random() * 1000
        })
    # save data to json file
    with open('generate_json/data.json', 'w') as f:
        json.dump(data, f)


# create a function that pass to the line each time we encounter { or } in json file and save it to a new file
def pretty_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)


# ------------------- main -------------------
generate_json()
pretty_json('generate_json/data.json')

# ------------------- test -------------------
# affiche les prenoms dans le fichier json
with open('generate_json/data.json', 'r') as f:
    data = json.load(f)
    for i in data:
        print(i['name'])
    
    
    ### test pour bechu xppppppp
    