from random import choice, randint
import time

# ------------------- les list -------------------
type_agv = ['Avant', 'Arriere']
etat_agv = ['En marche', 'libre']


# ------------------- generate csv -------------------
# creation a fucntion that generate and save data to a csv file, id, random choice in list names, country_names and a random age beetwen 18 and 65
def generate_csv():
    # open file
    with open('generate_csv/generation_csv_data.csv', 'w') as f:
        # write header to file
        f.write('id, type_agv, distance, temps, etat_agv, nbs_pieces')
        # loop for each line in data list in a new line
        for i in range(100):
            f.write('\n')
            # write id, random choice in type_agv, random disatnece, random temps, random choice etat_agv, random nbs_pieces
            f.write(f'{i+1}, {choice(type_agv)}, {randint(0,100)}, {randint(1,120)}, {choice(etat_agv)}, {randint(1,10)}')
            # time.sleep(3)
            # print data in console
            # print(f'{i+1}, {choice(type_agv)}, {randint(0,100)}, {randint(1,120)}, {choice(etat_agv)}, {randint(1,10)}')

generate_csv()