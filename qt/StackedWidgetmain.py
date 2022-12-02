from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow

from table_ihm import Ui_MainWindow

import sys
import time
# import the function data_to_dict from the file datafrommysql.py
from datafrommysql import data_to_dict

class window(QtWidgets.QMainWindow):
    def __init__ (self):
        self.main_win = QMainWindow()
        super(window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        self.tableau_machine_1()
        self.tableau_machine_2()
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)


        #connection des boutons
        self.ui.Machine1_2.clicked.connect(self.showMachine1)
        self.ui.Machine2_2.clicked.connect(self.showMachine2)
        self.ui.Machine3_2.clicked.connect(self.showMachine3)


    def show(self):
        self.main_win.show()

    def showMachine1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Machine1)

    def showMachine2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Machine2)

    def showMachine3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Machine3)

    #Tableau machine 1

    def tableau_machine_1(self):

        produits_machine_1 = data_to_dict()
    
        self.ui.tableWidget.setRowCount(len(produits_machine_1))
        self.ui.tableWidget.setColumnCount(len(produits_machine_1[0]))

        #init tables
        self.ui.tableWidget.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_1', 'etat_machine_2', 'etat_machine_3', 'etat_machine_4', 'nbs_pieces'))
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
            self.ui.tableWidget.setItem(nombre_produit,6,QTableWidgetItem(str(i['etat_machine_2'])))
            self.ui.tableWidget.setItem(nombre_produit,7,QTableWidgetItem(str(i['etat_machine_3'])))
            self.ui.tableWidget.setItem(nombre_produit,8,QTableWidgetItem(str(i['etat_machine_4'])))
            self.ui.tableWidget.setItem(nombre_produit,9,QTableWidgetItem(str(i['nbs_pieces'])))
            nombre_produit += 1

    #Tableau machine 2

    def tableau_machine_2(self):
        produits_machine_2 = data_to_dict()
        
        self.ui.tableWidget_2.setRowCount(len(produits_machine_2))
        self.ui.tableWidget_2.setColumnCount(len(produits_machine_2[0]))
        #init tables
        self.ui.tableWidget_2.setHorizontalHeaderLabels(('id', 'id_machine', 'type_agv', 'distance (m)', 'temps (s)', 'etat_machine_1', 'etat_machine_2', 'etat_machine_3', 'etat_machine_4', 'nbs_pieces'))
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
            self.ui.tableWidget_2.setItem(nombre_produit,5,QTableWidgetItem(str(i['etat_machine_1'])))
            self.ui.tableWidget_2.setItem(nombre_produit,6,QTableWidgetItem(str(i['etat_machine_2'])))
            self.ui.tableWidget_2.setItem(nombre_produit,7,QTableWidgetItem(str(i['etat_machine_3'])))
            self.ui.tableWidget_2.setItem(nombre_produit,8,QTableWidgetItem(str(i['etat_machine_4'])))
            self.ui.tableWidget_2.setItem(nombre_produit,9,QTableWidgetItem(str(i['nbs_pieces'])))

            nombre_produit += 1 


def main_ihm():
    app = QApplication(sys.argv)
    main_win = window()
    main_win.show()
    sys.exit(app.exec_())

main_ihm()