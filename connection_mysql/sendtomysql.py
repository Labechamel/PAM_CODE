import mysql.connector

# connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="pam"
)
# connect to a web host mysql
mydb = mysql.connector.connecct()

# create a cursor
mycursor = mydb.cursor()


#----------------------------------------
#create a function that read a csv file and insert data to mysql
def send_to_mysql():
    # open file
    with open('generate_csv/generation_csv_data.csv', 'r') as f:
        # read data from file
        data = f.read()
        # split data to a list
        data = data.split('\n')
        # remove header
        data.pop(0)
        # loop for each line in data list
        for line in data:
            # split line to a list
            line = line.split(',')
            # insert data to mysql
            mycursor.execute(f"INSERT INTO pam (id, type_agv, distance, temps, etat_agv, nbs_pieces) VALUES ('{line[0]}', '{line[1]}', '{line[2]}', '{line[3]}', '{line[4]}', '{line[5]}')")
            # commit
            mydb.commit()

# call function
send_to_mysql()

