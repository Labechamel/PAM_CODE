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
    column = ['id', 'type_agv', 'distance', 'temps', 'etat_agv', 'nbs_pieces']
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

# call function