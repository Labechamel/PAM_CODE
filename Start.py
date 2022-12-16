from connection_mysql.sendtomysql import *
from generate_csv.generation import *
from qt.IHMMachines import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow


def run():
    print("****************************************************************************************")
    print("                                      start                                             ")
    print("****************************************************************************************")
    print(' ')

    mydb, mycursor = connect_to_mysql()

    #drop_table()
    print (' ')
    print("----------------------------------------------------------------------------------------")
    print('                      we are connected to the database                                  ')
    print("----------------------------------------------------------------------------------------")
    print(' ')

    print('                 ---------> we send data to the database                                 ')
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print (' ')

    create_table(mydb, mycursor)
    init_csv()

    for i in range(1):
        generate_csv()    
    send_to_mysql(mydb, mycursor)
    print("----------------------------------------------------------------------------------------")
    print('                         data sent to the database                                      ')
    print("----------------------------------------------------------------------------------------")
    print(' ')

    print('         ------------> we collect data from the database                                ')
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print (' ')

    
    print("----------------------------------------------------------------------------------------")
    print('                  we have collected data from the database'                              )
    print("----------------------------------------------------------------------------------------")
    print(' ')
    
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(' ')
    print('                           we display the data                                          ')
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)

    mainIHM()



# create a function that ask in the terminal if you want drop the table pam and del the csv file
def main_nous():
    drop = input("Do you want to drop the table pam and the file generation_csv_data? (y/n) : ")
    if drop == "y":
        mydb, mycursor = connect_to_mysql()
        mycursor.execute("DROP TABLE pam")
        mydb.commit()
        print(' ')
        print("                                   table pam droped                                     ")
        print(' ')
        os.remove("generate_csv/generation_csv_data.csv")
        time.sleep(1)
        print("                          file generate_csv_data.csv deleted                            ")
        print(' ')
        print("****************************************************************************************")
        print(' ')
        
        time.sleep(1)
        drop2 = input("Do you want to create a new csv file (y/n)")
        print(' ')
        
        if drop2 == "y":
            init_csv()
            time.sleep(1)
            print("                             new csv file created                                       ")
            print("****************************************************************************************")
            print(' ')
            time.sleep(1)
            print("                          Now we run the program                                        ")
            print("****************************************************************************************")
            print (' ')
            print (' ')
            time.sleep(2)

            run()        
    else:
        run()

main_nous()