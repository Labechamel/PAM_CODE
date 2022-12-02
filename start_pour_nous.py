from connection_mysql.sendtomysql import *
from generate_csv.generation import *
from qt.IHMMachines import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow

# create a function that ask in the terminal if you want drop the table pam and del the csv file
#
def run():
    print("****************************************************************************************")
    print ("start")
    print(' ')

    mydb, mycursor = connect_to_mysql()

    #drop_table()
    print('we are connected to the database')
    print(' ')

    print('we send data to the database')
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)

    print(mydb, mycursor)
    create_table(mydb, mycursor)
    init_csv()

    #-----------------a decommenter si on utilise pas de threads------------------------------------#
    for i in range(1):
        generate_csv()    
    send_to_mysql(mydb, mycursor)
    print('data sent to the database')
    print(' ')

    print('we collect data from the database')
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('we have collected data from the database')
    print(' ')

    print('we display the data')
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)

    mainIHM()

    print("****************************************************************************************")


def main_nous():
    drop = input("Do you want to drop the table pam and the file generation_csv_data? (y/n)")
    if drop == "y":
        mydb, mycursor = connect_to_mysql()
        mycursor.execute("DROP TABLE pam")
        mydb.commit()
        print("table pam droped")
        os.remove("generate_csv/generation_csv_data.csv")
        print("file generate_csv_data.csv deleted")
        print("****************************************************************************************")
        drop2 = input("Do you want to create a new csv file (y/n)")
        if drop2 == "y":
            init_csv()
            print("new csv file created")
        print("****************************************************************************************")
        print("Now we run the program")
        print("****************************************************************************************")
        run()
    else:
        run()


main_nous()