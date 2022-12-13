from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QMainWindow
from qt.ui_IHMMachines import Ui_MainWindow
import sys
# import the function data_to_dict from the file datafrommysql.py
from qt.datafrommysql import *


class window(QtWidgets.QMainWindow):
      
        def __init__ (self):
                super(window,self).__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                #machine principale
                self.temps()
                self.vitesse()
                self.pieces()
                self.machines()
                self.nomTech()
                #machine secondaire
                self.machine1()
                self.machine2()
                self.machine3()
                self.machine4()
                
                #bouttons
                self.ui.pushButton.clicked.connect(self.showMachine1)
                #bouton1
                self.ui.Machine1_1.clicked.connect(self.showMachine1)
                self.ui.Machine1_2.clicked.connect(self.showMachine2)
                self.ui.Machine1_3.clicked.connect(self.showMachine3)
                self.ui.Machine1_4.clicked.connect(self.showMachine4)
                #bouton2
                self.ui.Machine2_1.clicked.connect(self.showMachine1)
                self.ui.Machine2_2.clicked.connect(self.showMachine2)
                self.ui.Machine2_3.clicked.connect(self.showMachine3)
                self.ui.Machine2_4.clicked.connect(self.showMachine4)
                #bouton3
                self.ui.Machine3_1.clicked.connect(self.showMachine1)
                self.ui.Machine3_2.clicked.connect(self.showMachine2)
                self.ui.Machine3_3.clicked.connect(self.showMachine3)
                self.ui.Machine3_4.clicked.connect(self.showMachine4)
                #bouton4
                self.ui.Machine4_1.clicked.connect(self.showMachine1)
                self.ui.Machine4_2.clicked.connect(self.showMachine2)
                self.ui.Machine4_3.clicked.connect(self.showMachine3)
                self.ui.Machine4_4.clicked.connect(self.showMachine4)
                #bouton2
                self.ui.Close_1.clicked.connect(self.showVide)
                self.ui.Close_2.clicked.connect(self.showVide)
                self.ui.Close_3.clicked.connect(self.showVide)
                self.ui.Close_4.clicked.connect(self.showVide)
                        #affichages
                        


        def showVide(self):
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.pagevide)

        def showMachine1(self):
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.Machine1)

        def showMachine2(self):
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.Machine2)

        def showMachine3(self):
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.Machine3)

        def showMachine4(self):
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.Machine4)


        # a changer
        def temps(self):
        #init tableau
                cycle = delete_column_keep_one(data_to_dict(),'id', 'id_machine', 'type_agv', 'distance', 'etat_machine_1', 'etat_machine_2', 'etat_machine_3', 'etat_machine_4', 'nbs_pieces')

                temps_moyen = two_decimal(calcul_average_time(cycle))
                self.ui.tableWidget_Temps.setRowCount(1)
                self.ui.tableWidget_Temps.setColumnCount(1)
                #init tables
                self.ui.tableWidget_Temps.setHorizontalHeaderLabels(('s',))
                #taille des colonnes
                self.ui.tableWidget_Temps.setColumnWidth(0,150)

                #boucle d'ajout
                nombre_produit= 0

                for i in cycle :
                        self.ui.tableWidget_Temps.setItem(0,nombre_produit,QTableWidgetItem(str(temps_moyen)))
                        nombre_produit += 1 
                        
        # a changer
        def vitesse(self):
                #init tableau
                vitesse = delete_column_keep_two(data_to_dict(),'id', 'id_machine', 'type_agv', 'etat_machine_1', 'etat_machine_2', 'etat_machine_3', 'etat_machine_4', 'nbs_pieces')

                vitesse_moyenne = two_decimal(calcul_average_speed(vitesse))
                self.ui.tableWidget_Vitesse.setRowCount(1)
                self.ui.tableWidget_Vitesse.setColumnCount(1)
                #init tables
                self.ui.tableWidget_Vitesse.setHorizontalHeaderLabels(('m/s',))
                #taille des colonnes
                self.ui.tableWidget_Vitesse.setColumnWidth(0,150)

                #boucle d'ajout
                nombre_produit= 0

                for i in vitesse :
                        self.ui.tableWidget_Vitesse.setItem(0,nombre_produit,QTableWidgetItem(str(vitesse_moyenne)))
                        nombre_produit += 1 
                        
        # a changer
        def pieces(self):
                #init tableau
                pieces = delete_column_keep_two(data_to_dict(),'id', 'id_machine', 'type_agv', 'distance', 'etat_machine_1', 'etat_machine_2', 'etat_machine_3', 'etat_machine_4')

                piece_minute = two_decimal(calcul_average_piece_per_minute(pieces))
                self.ui.tableWidget_Pieces.setRowCount(1)
                self.ui.tableWidget_Pieces.setColumnCount(1)
                #init tables
                self.ui.tableWidget_Pieces.setHorizontalHeaderLabels(('nbs pieces/min',))
                #taille des colonnes
                self.ui.tableWidget_Pieces.setColumnWidth(0,150)

                #boucle d'ajout
                nombre_produit= 0

                for i in pieces :
                        self.ui.tableWidget_Pieces.setItem(0,nombre_produit,QTableWidgetItem(str(piece_minute)))
                        nombre_produit += 1 
        
        def machines(self):
        #init tableau
                produits = delete_column_all_machine(data_to_dict(),'id_machine', 'type_agv', 'distance', 'temps', 'nbs_pieces')

                
                self.ui.tableWidget_Etat.setRowCount(len(produits))
                self.ui.tableWidget_Etat.setColumnCount(len(produits[0]))
                #init tables
                self.ui.tableWidget_Etat.setHorizontalHeaderLabels(('Machine 1','Machine 2','Machine 3','Machine 4'))
                
                #taille des colonnes
                self.ui.tableWidget_Etat.setColumnWidth(0,100)
                self.ui.tableWidget_Etat.setColumnWidth(1,100)
                self.ui.tableWidget_Etat.setColumnWidth(2,100)
                self.ui.tableWidget_Etat.setColumnWidth(3,100)
                
                #boucle d'ajout
                nombre_produit= 0

                for i in produits :
                        self.ui.tableWidget_Etat.setItem(nombre_produit,0,QTableWidgetItem(str(i['etat_machine_1'])))
                        self.ui.tableWidget_Etat.setItem(nombre_produit,1,QTableWidgetItem(str(i['etat_machine_2'])))
                        self.ui.tableWidget_Etat.setItem(nombre_produit,2,QTableWidgetItem(str(i['etat_machine_3'])))
                        self.ui.tableWidget_Etat.setItem(nombre_produit,3,QTableWidgetItem(str(i['etat_machine_4'])))
                        nombre_produit += 1 


        def nomTech(self):
        #init tableau
                produits = [ 
                        {'Machine 1':'Abel','Machine 2':'Pierre', 'Machine 3':'Marie', 'Machine 4':'Victor',},
                        {'Machine 1':'Abel','Machine 2':'Pierre', 'Machine 3':'Marie', 'Machine 4':'Paul',},]
                
                self.ui.tableWidget_Technicien.setRowCount(len(produits))
                self.ui.tableWidget_Technicien.setColumnCount(4)
                #init tables
                self.ui.tableWidget_Technicien.setHorizontalHeaderLabels(('Machine 1','Machine 2','Machine 3','Machine 4'))
                
                #taille des colonnes
                self.ui.tableWidget_Technicien.setColumnWidth(0,100)
                self.ui.tableWidget_Technicien.setColumnWidth(1,100)
                self.ui.tableWidget_Technicien.setColumnWidth(2,100)
                self.ui.tableWidget_Technicien.setColumnWidth(3,100)
                
                #boucle d'ajout
                nombre_produit= 0

                for i in produits :
                        self.ui.tableWidget_Technicien.setItem(nombre_produit,0,QTableWidgetItem(str(i['Machine 1'])))
                        self.ui.tableWidget_Technicien.setItem(nombre_produit,1,QTableWidgetItem(str(i['Machine 2'])))
                        self.ui.tableWidget_Technicien.setItem(nombre_produit,2,QTableWidgetItem(str(i['Machine 3'])))
                        self.ui.tableWidget_Technicien.setItem(nombre_produit,3,QTableWidgetItem(str(i['Machine 4'])))
                        nombre_produit += 1 
        ###-----------------------------------------------------------------------------------------------------------------------------------------------------------###
                ##Details##

        #Tableau1

        def machine1(self):
                produits_machine_1 =delete_column_machine(data_to_dict(),'etat_machine_2', 'etat_machine_3', 'etat_machine_4')

                
                self.ui.tableWidget_Machine1.setRowCount(len(produits_machine_1))
                self.ui.tableWidget_Machine1.setColumnCount(len(produits_machine_1[0]))

                #init tables
                self.ui.tableWidget_Machine1.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_1', 'nbs_pieces'))
                #taille des colonnes
                self.ui.tableWidget_Machine1.setColumnWidth(0,50)
                self.ui.tableWidget_Machine1.setColumnWidth(1,150)
                self.ui.tableWidget_Machine1.setColumnWidth(2,150)
                self.ui.tableWidget_Machine1.setColumnWidth(3,150)
                #boucle d'ajout
                nombre_produit= 0

                # on parcourt la liste des produits et on ajoute les données dans le tableau
                for i in produits_machine_1 :
                        
                        self.ui.tableWidget_Machine1.setItem(nombre_produit,0,QTableWidgetItem(str(i['id'])))
                        self.ui.tableWidget_Machine1.setItem(nombre_produit,1,QTableWidgetItem(str(i['id_machine'])))

                        self.ui.tableWidget_Machine1.setItem(nombre_produit,2,QTableWidgetItem(str(i['type_agv'])))
                        self.ui.tableWidget_Machine1.setItem(nombre_produit,3,QTableWidgetItem(str(i['distance'])))
                        self.ui.tableWidget_Machine1.setItem(nombre_produit,4,QTableWidgetItem(str(i['temps'])))
                        self.ui.tableWidget_Machine1.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_1'])))
                        self.ui.tableWidget_Machine1.setItem(nombre_produit,6,QTableWidgetItem(str(i['nbs_pieces'])))
                        nombre_produit += 1


                #machine2

        def machine2(self):
                produits_machine_2 =delete_column_machine(data_to_dict(),'etat_machine_1', 'etat_machine_3', 'etat_machine_4')
                        
                self.ui.tableWidget_Machine2.setRowCount(len(produits_machine_2))
                self.ui.tableWidget_Machine2.setColumnCount(len(produits_machine_2[0]))
                #init tables
                self.ui.tableWidget_Machine2.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_2', 'nbs_pieces'))
                #taille des colonnes
                self.ui.tableWidget_Machine2.setColumnWidth(0,50)
                self.ui.tableWidget_Machine2.setColumnWidth(1,150)
                self.ui.tableWidget_Machine2.setColumnWidth(2,150)
                self.ui.tableWidget_Machine2.setColumnWidth(3,150)
                #boucle d'ajout
                nombre_produit= 0

                for i in produits_machine_2 :

                        self.ui.tableWidget_Machine2.setItem(nombre_produit,0,QTableWidgetItem(str(i['id'])))
                        self.ui.tableWidget_Machine2.setItem(nombre_produit,1,QTableWidgetItem(str(i['id_machine'])))
                        self.ui.tableWidget_Machine2.setItem(nombre_produit,2,QTableWidgetItem(str(i['type_agv'])))
                        self.ui.tableWidget_Machine2.setItem(nombre_produit,3,QTableWidgetItem(str(i['distance'])))
                        self.ui.tableWidget_Machine2.setItem(nombre_produit,4,QTableWidgetItem(str(i['temps'])))
                        self.ui.tableWidget_Machine2.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_2'])))
                        self.ui.tableWidget_Machine2.setItem(nombre_produit,6,QTableWidgetItem(str(i['nbs_pieces'])))

                        nombre_produit += 1 


                #machine3

        def machine3(self):
                produits_machine_3 =delete_column_machine(data_to_dict(),'etat_machine_1', 'etat_machine_2', 'etat_machine_4')

                        
                self.ui.tableWidget_Machine3.setRowCount(len(produits_machine_3))
                self.ui.tableWidget_Machine3.setColumnCount(len(produits_machine_3[0]))
                #init tables
                self.ui.tableWidget_Machine3.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_3', 'nbs_pieces'))
                #taille des colonnes
                self.ui.tableWidget_Machine3.setColumnWidth(0,50)
                self.ui.tableWidget_Machine3.setColumnWidth(1,150)
                self.ui.tableWidget_Machine3.setColumnWidth(2,150)
                self.ui.tableWidget_Machine3.setColumnWidth(3,150)
                #boucle d'ajout
                nombre_produit= 0

                for i in produits_machine_3 :

                        self.ui.tableWidget_Machine3.setItem(nombre_produit,0,QTableWidgetItem(str(i['id'])))
                        self.ui.tableWidget_Machine3.setItem(nombre_produit,1,QTableWidgetItem(str(i['id_machine'])))
                        self.ui.tableWidget_Machine3.setItem(nombre_produit,2,QTableWidgetItem(str(i['type_agv'])))
                        self.ui.tableWidget_Machine3.setItem(nombre_produit,3,QTableWidgetItem(str(i['distance'])))
                        self.ui.tableWidget_Machine3.setItem(nombre_produit,4,QTableWidgetItem(str(i['temps'])))
                        self.ui.tableWidget_Machine3.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_3'])))
                        self.ui.tableWidget_Machine3.setItem(nombre_produit,6,QTableWidgetItem(str(i['nbs_pieces'])))

                        nombre_produit += 1 

                #machine4

        def machine4(self):
                produits_machine_4 =delete_column_machine(data_to_dict(),'etat_machine_1', 'etat_machine_2', 'etat_machine_3')

                        
                self.ui.tableWidget_Machine4.setRowCount(len(produits_machine_4))
                self.ui.tableWidget_Machine4.setColumnCount(len(produits_machine_4[0]))
                #init tables
                self.ui.tableWidget_Machine4.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_4', 'nbs_pieces'))
                #taille des colonnes
                self.ui.tableWidget_Machine4.setColumnWidth(0,50)
                self.ui.tableWidget_Machine4.setColumnWidth(1,150)
                self.ui.tableWidget_Machine4.setColumnWidth(2,150)
                self.ui.tableWidget_Machine4.setColumnWidth(3,150)
                #boucle d'ajout
                nombre_produit= 0

                for i in produits_machine_4 :

                        self.ui.tableWidget_Machine4.setItem(nombre_produit,0,QTableWidgetItem(str(i['id'])))
                        self.ui.tableWidget_Machine4.setItem(nombre_produit,1,QTableWidgetItem(str(i['id_machine'])))
                        self.ui.tableWidget_Machine4.setItem(nombre_produit,2,QTableWidgetItem(str(i['type_agv'])))
                        self.ui.tableWidget_Machine4.setItem(nombre_produit,3,QTableWidgetItem(str(i['distance'])))
                        self.ui.tableWidget_Machine4.setItem(nombre_produit,4,QTableWidgetItem(str(i['temps'])))
                        self.ui.tableWidget_Machine4.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_4'])))
                        self.ui.tableWidget_Machine4.setItem(nombre_produit,6,QTableWidgetItem(str(i['nbs_pieces'])))

                        nombre_produit += 1 

##-------------------------------------------------------------------------------------------------------------------------------------------------------------------##
##lecture##
def mainIHM():
        app = QtWidgets.QApplication(sys.argv)
        win = window()
        win.show()
        sys.exit(app.exec_())
