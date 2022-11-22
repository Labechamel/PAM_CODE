from random import choice, randint, uniform
from function import generate_list_from_txt

# ------------------- les list -------------------
name = generate_list_from_txt()
# create a list with 30 countries 
country_names = [ 'France', 'Germany', 'Italy', 'Spain', 'Portugal', 'Belgium', 'Netherlands', 'Luxembourg', 'Switzerland', 'Austria', 'Poland', 'Czech Republic', 'Slovakia', 'Hungary', 'Romania', 'Bulgaria', 'Greece', 'Turkey', 'Bosnia and Herzegovina', 'Serbia', 'Montenegro', 'Macedonia', 'Albania', 'Croatia', 'Slovenia', 'Moldova', 'Ukraine', 'Belarus', 'Russia', 'Kazakhstan', 'China', 'Japan', 'South Korea', 'North Korea', 'Vietnam', 'Thailand', 'Laos', 'Cambodia', 'Myanmar', 'Malaysia', 'Indonesia', 'Philippines', 'Singapore', 'Brunei', 'Australia', 'New Zealand', 'India', 'Pakistan', 'Afghanistan', 'Iran', 'Iraq', 'Saudi Arabia', 'Yemen', 'Oman', 'United Arab Emirates', 'Qatar', 'Bahrain', 'Kuwait']


# ------------------- generate csv -------------------
# creation a fucntion that generate and save data to a csv file, id, random choice in list names, country_names and a random age beetwen 18 and 65
def generate_csv():
    # open file
    with open('generate_csv/generation_csv_data.csv', 'w') as f:
        # write header to file
        f.write('id, name, country, age')
        # loop for each line in data list in a new line
        for i in range(10):
            f.write('\n')
            # write id, random choice in list names, country_names and a random age beetwen 18 and 65
            f.write(f'{i}, {choice(name)}, {choice(country_names)}, {randint(18, 65)}')
        


generate_csv()