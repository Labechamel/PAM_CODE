# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StackedWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(60, 40, 681, 421))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Machine1 = QtWidgets.QWidget()
        self.Machine1.setObjectName("Machine1")
        self.label = QtWidgets.QLabel(self.Machine1)
        self.label.setGeometry(QtCore.QRect(340, 10, 47, 13))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.Machine1)
        self.tableWidget.setGeometry(QtCore.QRect(80, 70, 561, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.stackedWidget.addWidget(self.Machine1)
        self.Machine2 = QtWidgets.QWidget()
        self.Machine2.setObjectName("Machine2")
        self.label_2 = QtWidgets.QLabel(self.Machine2)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.Machine2)
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.checkBox = QtWidgets.QCheckBox(self.home)
        self.checkBox.setGeometry(QtCore.QRect(250, 160, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.home)
        self.Machine3 = QtWidgets.QWidget()
        self.Machine3.setStyleSheet("")
        self.Machine3.setObjectName("Machine3")
        self.label_3 = QtWidgets.QLabel(self.Machine3)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 47, 13))
        self.label_3.setObjectName("label_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Machine3)
        self.tableWidget_2.setGeometry(QtCore.QRect(80, 70, 551, 331))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.stackedWidget.addWidget(self.Machine3)
        self.Machine1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Machine1_2.setGeometry(QtCore.QRect(70, 500, 75, 23))
        self.Machine1_2.setObjectName("Machine1_2")
        self.Machine2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Machine2_2.setGeometry(QtCore.QRect(350, 500, 75, 23))
        self.Machine2_2.setObjectName("Machine2_2")
        self.Machine3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Machine3_2.setGeometry(QtCore.QRect(640, 500, 75, 23))
        self.Machine3_2.setObjectName("Machine3_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Machine1"))
        self.label_2.setText(_translate("MainWindow", "Machine 2"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label_3.setText(_translate("MainWindow", "Machine3"))
        self.Machine1_2.setText(_translate("MainWindow", "Machine 1"))
        self.Machine2_2.setText(_translate("MainWindow", "Machine 2"))
        self.Machine3_2.setText(_translate("MainWindow", "Machine 3"))

