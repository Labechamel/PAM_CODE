from connection_mysql.sendtomysql import *
from generate_csv.generation import *
from threading import Thread
#from qt.IHM.StackedWidgetmain import *

def generate_data(mydb, mycursor):
    #lancement = True #pour initialiser la variable lancement 
    while True: #lancement == True pour stopper depuis l'IHM
        generate_csv()
        send_to_mysql(mydb, mycursor)
        time.sleep(5)
    
print ("start")
mydb, mycursor = connect_to_mysql()

#drop_table()
print('hello')
print(mydb, mycursor)
create_table(mydb, mycursor)
init_csv()

#-----------------a decommenter si on utilise pas de threads------------------------------------#
for i in range(1):
    generate_csv()    
send_to_mysql(mydb, mycursor)
#mainIHM()  #presente dans stackedwidgetmain.py
#--------------------------------------------------------------------------------#


# utilisation de threads pour comportement proche simulateur reel
#-----------------------------------------------------------------------

# a = Thread(target = generate_data(mydb, mycursor))
# b = Thread(target = mainIHM()) #main IHM replace "if __name__== '__main__':" by "def main():" in StackedWidgetmain.py
# a.start()
# b.start()  

#--------------------------------------------------------------------------------#