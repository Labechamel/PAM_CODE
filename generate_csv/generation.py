from random import choice, randint
import time

# ------------------- les list -------------------
type_agv = ['Avant', 'Arriere']
etat_agv = ['Libre','En marche']
distance_chemin = [24,15,18,20,16,22,19,22]


# ------------------- generate csv -------------------
# creation a fucntion that generate and save data to a csv file, id, random choice in list names, country_names and a random age beetwen 18 and 65
def generate_csv():
    # open file
    with open('generate_csv/generation_csv_data.csv', 'w') as f:
        # write header to file
        f.write('id_machine, type_agv, distance, temps, etat_machine_1, etat_machine_2, etat_machine_3, etat_machine_4, nbs_pieces')
        # loop for each line in data list in a new line
        for i in range(30):
            agv_type = choice(type_agv)
            if agv_type == 'Avant':
                distance1 = distance_chemin[0]
                distance2 = distance_chemin[1]
                distance3 = distance_chemin[2]
                distance4 = distance_chemin[3]

            else:
                distance1 = distance_chemin[4]
                distance2 = distance_chemin[5]
                distance3 = distance_chemin[6]
                distance4 = distance_chemin[7]

            
            a = 1
            b = 0

            f.write('\n')
            # write id, random choice in type_agv, random disatnece, random temps, random choice etat_agv, random nbs_pieces
            f.write(f'{i+1}, {agv_type}, {distance1}, {randint(90,120)}, {etat_agv[a]}, {etat_agv[b]}, {etat_agv[b]}, {etat_agv[b]}, {randint(1,10)}')
            f.write('\n')
            f.write(f'{i+1}, {agv_type}, {distance2}, {randint(90,120)}, {etat_agv[b]}, {etat_agv[a]}, {etat_agv[b]}, {etat_agv[b]}, {randint(1,10)}')
            f.write('\n')
            f.write(f'{i+1}, {agv_type}, {distance3}, {randint(90,120)}, {etat_agv[b]}, {etat_agv[b]}, {etat_agv[a]}, {etat_agv[b]}, {randint(1,10)}')
            f.write('\n')
            f.write(f'{i+1}, {agv_type}, {distance4}, {randint(90,120)}, {etat_agv[b]}, {etat_agv[b]}, {etat_agv[b]}, {etat_agv[a]}, {randint(1,10)}')



generate_csv()