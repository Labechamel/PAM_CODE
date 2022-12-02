from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow
from qt.ui_IHMMachines import Ui_MainWindow

import sys
import time

# import the function data_to_dict from the file datafrommysql.py
from qt.datafrommysql import *

class window(QtWidgets.QMainWindow):
    def __init__ (self):
        self.main_win = QMainWindow()
        super(window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.tableau_machine_1()
        self.tableau_machine_2()
        self.tableau_machine_3()
        self.tableau_machine_4()
       



        self.ui.stackedWidget.setCurrentWidget(self.ui.Machine1)

        #coonections des boutons
        self.ui.Machine1_2.clicked.connect(self.showMachine1)
        self.ui.Machine2_2.clicked.connect(self.showMachine2)
        self.ui.Machine3_2.clicked.connect(self.showMachine3)
        self.ui.Machine3_3.clicked.connect(self.showMachine4)
        self.ui.Close.clicked.connect(self.closeEvent)

    def show(self):
        self.main_win.show()

    def showMachine1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Machine1)

    def showMachine2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Machine2)

    def showMachine3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Machine3)
    
    def showMachine4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Machine4)

    #Tableau machine 1

    def tableau_machine_1(self):
        
        produits_machine_1 =delete_column(data_to_dict(),'etat_machine_2', 'etat_machine_3', 'etat_machine_4')

    
        self.ui.tableWidget.setRowCount(len(produits_machine_1))
        self.ui.tableWidget.setColumnCount(len(produits_machine_1[0]))

        #init tables
        self.ui.tableWidget.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_1', 'nbs_pieces'))
        #taille des colonnes
        self.ui.tableWidget.setColumnWidth(0,50)
        self.ui.tableWidget.setColumnWidth(1,150)
        self.ui.tableWidget.setColumnWidth(2,150)
        self.ui.tableWidget.setColumnWidth(3,150)
         #boucle d'ajout
        nombre_produit= 0

        # on parcourt la liste des produits et on ajoute les données dans le tableau
        for i in produits_machine_1 :
                
            self.ui.tableWidget.setItem(nombre_produit,0,QTableWidgetItem(str(i['id'])))
            self.ui.tableWidget.setItem(nombre_produit,1,QTableWidgetItem(str(i['id_machine'])))

            self.ui.tableWidget.setItem(nombre_produit,2,QTableWidgetItem(str(i['type_agv'])))
            self.ui.tableWidget.setItem(nombre_produit,3,QTableWidgetItem(str(i['distance'])))
            self.ui.tableWidget.setItem(nombre_produit,4,QTableWidgetItem(str(i['temps'])))
            self.ui.tableWidget.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_1'])))
            self.ui.tableWidget.setItem(nombre_produit,6,QTableWidgetItem(str(i['nbs_pieces'])))
            nombre_produit += 1

    #Tableau2

    def tableau_machine_2(self):
        
        produits_machine_2 =delete_column(data_to_dict(),'etat_machine_1', 'etat_machine_3', 'etat_machine_4')
        
        self.ui.tableWidget_2.setRowCount(len(produits_machine_2))
        self.ui.tableWidget_2.setColumnCount(len(produits_machine_2[0]))
        #init tables
        self.ui.tableWidget_2.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_2', 'nbs_pieces'))
        #taille des colonnes
        self.ui.tableWidget_2.setColumnWidth(0,50)
        self.ui.tableWidget_2.setColumnWidth(1,150)
        self.ui.tableWidget_2.setColumnWidth(2,150)
        self.ui.tableWidget_2.setColumnWidth(3,150)
        #boucle d'ajout
        nombre_produit= 0

        for i in produits_machine_2 :

            self.ui.tableWidget_2.setItem(nombre_produit,0,QTableWidgetItem(str(i['id'])))
            self.ui.tableWidget_2.setItem(nombre_produit,1,QTableWidgetItem(str(i['id_machine'])))
            self.ui.tableWidget_2.setItem(nombre_produit,2,QTableWidgetItem(str(i['type_agv'])))
            self.ui.tableWidget_2.setItem(nombre_produit,3,QTableWidgetItem(str(i['distance'])))
            self.ui.tableWidget_2.setItem(nombre_produit,4,QTableWidgetItem(str(i['temps'])))
            self.ui.tableWidget_2.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_2'])))
            self.ui.tableWidget_2.setItem(nombre_produit,6,QTableWidgetItem(str(i['nbs_pieces'])))

            nombre_produit += 1 


    #Tableau3

    def tableau_machine_3(self):
        produits_machine_3 =delete_column(data_to_dict(),'etat_machine_1', 'etat_machine_2', 'etat_machine_4')

        
        self.ui.tableWidget_3.setRowCount(len(produits_machine_3))
        self.ui.tableWidget_3.setColumnCount(len(produits_machine_3[0]))
        #init tables
        self.ui.tableWidget_3.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_3', 'nbs_pieces'))
        #taille des colonnes
        self.ui.tableWidget_3.setColumnWidth(0,50)
        self.ui.tableWidget_3.setColumnWidth(1,150)
        self.ui.tableWidget_3.setColumnWidth(2,150)
        self.ui.tableWidget_3.setColumnWidth(3,150)
        #boucle d'ajout
        nombre_produit= 0

        for i in produits_machine_3 :

            self.ui.tableWidget_3.setItem(nombre_produit,0,QTableWidgetItem(str(i['id'])))
            self.ui.tableWidget_3.setItem(nombre_produit,1,QTableWidgetItem(str(i['id_machine'])))
            self.ui.tableWidget_3.setItem(nombre_produit,2,QTableWidgetItem(str(i['type_agv'])))
            self.ui.tableWidget_3.setItem(nombre_produit,3,QTableWidgetItem(str(i['distance'])))
            self.ui.tableWidget_3.setItem(nombre_produit,4,QTableWidgetItem(str(i['temps'])))
            self.ui.tableWidget_3.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_3'])))
            self.ui.tableWidget_3.setItem(nombre_produit,6,QTableWidgetItem(str(i['nbs_pieces'])))

            nombre_produit += 1 

#Tableau4

    def tableau_machine_4(self):
        produits_machine_4 =delete_column(data_to_dict(),'etat_machine_1', 'etat_machine_2', 'etat_machine_3')

        
        self.ui.tableWidget_4.setRowCount(len(produits_machine_4))
        self.ui.tableWidget_4.setColumnCount(len(produits_machine_4[0]))
        #init tables
        self.ui.tableWidget_4.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_4', 'nbs_pieces'))
        #taille des colonnes
        self.ui.tableWidget_4.setColumnWidth(0,50)
        self.ui.tableWidget_4.setColumnWidth(1,150)
        self.ui.tableWidget_4.setColumnWidth(2,150)
        self.ui.tableWidget_4.setColumnWidth(3,150)
        #boucle d'ajout
        nombre_produit= 0

        for i in produits_machine_4 :

            self.ui.tableWidget_4.setItem(nombre_produit,0,QTableWidgetItem(str(i['id'])))
            self.ui.tableWidget_4.setItem(nombre_produit,1,QTableWidgetItem(str(i['id_machine'])))
            self.ui.tableWidget_4.setItem(nombre_produit,2,QTableWidgetItem(str(i['type_agv'])))
            self.ui.tableWidget_4.setItem(nombre_produit,3,QTableWidgetItem(str(i['distance'])))
            self.ui.tableWidget_4.setItem(nombre_produit,4,QTableWidgetItem(str(i['temps'])))
            self.ui.tableWidget_4.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_4'])))
            self.ui.tableWidget_4.setItem(nombre_produit,6,QTableWidgetItem(str(i['nbs_pieces'])))

            nombre_produit += 1 


def mainIHM():
    app = QApplication(sys.argv)
    main_win = window()
    main_win.show()
    sys.exit(app.exec_())