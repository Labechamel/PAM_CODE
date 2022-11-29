import mysql.connector

# connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="pam"
)
# create a cursor
mycursor = mydb.cursor()


#----------------------------------------
# create a function that create a table 'pam' with id INT NOT NULL, type_agv VARCHAR(255) NOT NULL, distance INT NOT NULL,temps INT NOT NULL, etat_agv VARCHAR(255) NOT NULL, nbs_pieces INT NOT NULL, PRIMARY KEY (id) 
def create_table():
    # create table
    mycursor.execute("CREATE TABLE pam (id INT NOT NULL, type_agv VARCHAR(255) NOT NULL, distance INT NOT NULL,temps INT NOT NULL, etat_agv VARCHAR(255) NOT NULL, nbs_pieces INT NOT NULL, PRIMARY KEY (id))")
    # commit
    mydb.commit()


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


# create a fucntion that drop table 'pam'
def drop_table():
    # drop table
    mycursor.execute("DROP TABLE pam")
    # commit
    mydb.commit()


# call function
drop_table()
create_table()
send_to_mysql()