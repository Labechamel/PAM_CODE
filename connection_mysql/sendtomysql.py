import mysql.connector

# créer une fonction qui se connecte à la base de données
def connect_to_mysql():
    # connect to mysql
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="pam"
    )   

    mycursor = mydb.cursor()
    return mydb, mycursor



#----------------------------------------
# create a function that create a table 'pam' with id INT NOT NULL, type_agv VARCHAR(255) NOT NULL, distance INT NOT NULL,temps INT NOT NULL, etat_agv VARCHAR(255) NOT NULL, nbs_pieces INT NOT NULL, PRIMARY KEY (id) 
def create_table(mydb, mycursor):
    # verifier si la table "pam" existe deja
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    if ('pam',) not in tables:
        mycursor.execute("CREATE TABLE pam (id INT NOT NULL AUTO_INCREMENT, id_machine INT NOT NULL, type_agv VARCHAR(255) NOT NULL, distance INT NOT NULL,temps INT NOT NULL, etat_machine_1 VARCHAR(255) NOT NULL, etat_machine_2 VARCHAR(255) NOT NULL, etat_machine_3 VARCHAR(255) NOT NULL, etat_machine_4 VARCHAR(255) NOT NULL, nbs_pieces INT NOT NULL, PRIMARY KEY (id))")
        mydb.commit()  # commit
        
        
#----------------------------------------

#create a function that read a csv file and insert data to mysql
def send_to_mysql(mydb, mycursor):
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
            mycursor.execute(f"INSERT INTO pam (id_machine, type_agv, distance, temps, etat_machine_1, etat_machine_2, etat_machine_3, etat_machine_4, nbs_pieces) VALUES ('{line[0]}', '{line[1]}', '{line[2]}', '{line[3]}', '{line[4]}', '{line[5]}', '{line[6]}', '{line[7]}', '{line[8]}')")
            # commit
            mydb.commit()


# create a fucntion that drop table 'pam'
def drop_table(mydb, mycursor):
    # drop table
    mycursor.execute("DROP TABLE pam")
    # commit
    mydb.commit()
