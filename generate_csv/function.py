import os
import sys
# ------------------- function -------------------

def generate_list_from_txt():
    # open file
    with open(os.path.join(sys.path[0],"generate_name\list_name.txt"), 'r') as f:
        # read file and save data to a list
        data = f.readlines()
        # create a dictionary
        liste = []
        # loop for each line in data list
        for line in data:
            # add value to dictionary withouth space and simply one time
            liste.append(line.strip())
    # return result
    return liste


# save result to a txt file
def save():
    with open(os.path.join(sys.path[0],"generate_name\generationdict_name.txt"), 'w') as f:
        # write result to file
        f.write(str(generate_list_from_txt()))