import mysql.connector

# on se connect à la base de données
# connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="pam"
)

# create a cursor
mycursor = mydb.cursor()

# create a fucntion that read data from mysql from the table 'pam' and return a list of data
def read_from_mysql():
    # read data from mysql
    mycursor.execute("SELECT * FROM pam")
    # fetch data
    data = mycursor.fetchall()
    # return data
    return data

# create a function that associate all [i][0] the name of the column to the data
def data_to_dict():
    # call function
    data = read_from_mysql()
    # create a list of name of the column
    column = ['id', 'id_machine', 'type_agv', 'distance', 'temps', 'etat_machine_1', 'etat_machine_2', 'etat_machine_3', 'etat_machine_4', 'nbs_pieces']
    # create a list of data
    data_list = []
    # loop for each line in data
    for line in data:
        # create a dict
        data_dict = {}
        # loop for each column in column
        for i in range(len(column)):
            # associate the name of the column to the data
            data_dict[column[i]] = line[i]
        # append data to data_list
        data_list.append(data_dict)
    # return data_list
    return data_list


# create a function that take 3 columns in argument and delete them from the list of data_to_dict
def delete_column_machine(list, column1, column2, column3):
    # call function
    data = list
    # loop for each line in data
    for line in data:
        # delete the column1
        del line[column1]
        # delete the column2
        del line[column2]
        # delete the column3
        del line[column3]
    # return data
    return data

def delete_column_all_machine(list, column1, column2, column3, column4, column5):
    # call function
    data = list
    # loop for each line in data
    for line in data:
        # delete the column1
        del line[column1]
        # delete the column2
        del line[column2]
        # delete the column3
        del line[column3]
        # delete the column4
        del line[column4]
        # delete the column5
        del line[column5]
    # return data
    return data

def delete_column_keep_two(list, column1, column2, column3, column4, column5, column6, column7, column8):
    # call function
    data = list
    # loop for each line in data
    for line in data:
        # delete the column1
        del line[column1]
        # delete the column2
        del line[column2]
        # delete the column3
        del line[column3]
        # delete the column4
        del line[column4]
        # delete the column5
        del line[column5]
        # delete the column6
        del line[column6]
        # delete the column7
        del line[column7]
        # delete the column8
        del line[column8]
    # return data
    return data

def delete_column_keep_one(list, column1, column2, column3, column4, column5, column6, column7, column8, column9):
    # call function
    data = list
    # loop for each line in data
    for line in data:
        # delete the column1
        del line[column1]
        # delete the column2
        del line[column2]
        # delete the column3
        del line[column3]
        # delete the column4
        del line[column4]
        # delete the column5
        del line[column5]
        # delete the column6
        del line[column6]
        # delete the column7
        del line[column7]
        # delete the column8
        del line[column8]
        # delete the column9
        del line[column9]
    # return data
    return data

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# function de calcul

def calcul_average_time(list):
    # call function
    data = list
    # create a list of time
    time = []
    # loop for each line in data
    for line in data:
        # append the time to time
        time.append(line['temps'])
    # calcul the average of time
    average_time = sum(time)/len(time)
    # return average_time
    return average_time

# create a fucntion that calcul the average of speed 
def calcul_average_speed(list):
    # call function
    data = list
    # create a list of speed
    speed = []
    # loop for each line in data
    for line in data:
        # calcul the speed
        speed.append(line['distance']/line['temps'])
    # calcul the average of speed
    average_speed = sum(speed)/len(speed)
    # return average_speed
    return average_speed

# create a function that calcul the average of piece per minute
def calcul_average_piece_per_minute(list):
    # call function
    data = list
    # create a list of piece per minute
    piece_per_minute = []
    # loop for each line in data
    for line in data:
        # convert the time in minute
        line['temps'] = line['temps']/60
        # calcul the piece per minute
        piece_per_minute.append(line['nbs_pieces']/line['temps'])
    # calcul the average of piece per minute
    average_piece_per_minute = sum(piece_per_minute)/len(piece_per_minute)
    # return average_piece_per_minute
    return average_piece_per_minute