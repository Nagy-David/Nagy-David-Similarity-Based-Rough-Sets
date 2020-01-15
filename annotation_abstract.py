# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'annotation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 494)
        self.listOfBaseSets = QtWidgets.QTextEdit(Dialog)
        self.listOfBaseSets.setGeometry(QtCore.QRect(20, 240, 321, 231))
        self.listOfBaseSets.setObjectName("listOfBaseSets")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 220, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 111, 16))
        self.label_3.setObjectName("label_3")
        self.singleton_id = QtWidgets.QTextEdit(Dialog)
        self.singleton_id.setGeometry(QtCore.QRect(350, 30, 61, 31))
        self.singleton_id.setObjectName("singleton_id")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 30, 81, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(280, 80, 61, 16))
        self.label_5.setObjectName("label_5")
        self.cluster_id = QtWidgets.QTextEdit(Dialog)
        self.cluster_id.setGeometry(QtCore.QRect(350, 70, 61, 31))
        self.cluster_id.setObjectName("cluster_id")
        self.insertButton = QtWidgets.QPushButton(Dialog)
        self.insertButton.setGeometry(QtCore.QRect(280, 120, 75, 23))
        self.insertButton.setObjectName("insertButton")
        self.listOfSingletons = QtWidgets.QListWidget(Dialog)
        self.listOfSingletons.setGeometry(QtCore.QRect(20, 30, 101, 171))
        self.listOfSingletons.setObjectName("listOfSingletons")
        self.listOfClusterIDs = QtWidgets.QListWidget(Dialog)
        self.listOfClusterIDs.setGeometry(QtCore.QRect(160, 30, 91, 171))
        self.listOfClusterIDs.setObjectName("listOfClusterIDs")
        self.applyButton = QtWidgets.QPushButton(Dialog)
        self.applyButton.setGeometry(QtCore.QRect(420, 30, 91, 23))
        self.applyButton.setObjectName("applyButton")
        self.helpButton = QtWidgets.QPushButton(Dialog)
        self.helpButton.setGeometry(QtCore.QRect(370, 120, 75, 23))
        self.helpButton.setObjectName("helpButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>The list of base sets:</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>The list of singletons</p><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>The list of cluster IDs</p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Singleton ID:"))
        self.label_5.setText(_translate("Dialog", "Cluster ID:"))
        self.insertButton.setText(_translate("Dialog", "Insert"))
        self.applyButton.setText(_translate("Dialog", "Apply and Exit"))
        self.helpButton.setText(_translate("Dialog", "Help"))

