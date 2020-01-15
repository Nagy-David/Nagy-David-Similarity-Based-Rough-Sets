# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'approximation.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(662, 406)
        self.points_canvas = QtWidgets.QGraphicsView(Dialog)
        self.points_canvas.setGeometry(QtCore.QRect(30, 80, 591, 301))
        self.points_canvas.setObjectName("points_canvas")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(560, 10, 75, 23))
        self.okButton.setObjectName("okButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 511, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.printSetButton = QtWidgets.QPushButton(self.layoutWidget)
        self.printSetButton.setObjectName("printSetButton")
        self.horizontalLayout.addWidget(self.printSetButton)
        self.printLowerButton = QtWidgets.QPushButton(self.layoutWidget)
        self.printLowerButton.setObjectName("printLowerButton")
        self.horizontalLayout.addWidget(self.printLowerButton)
        self.printUpperButton = QtWidgets.QPushButton(self.layoutWidget)
        self.printUpperButton.setObjectName("printUpperButton")
        self.horizontalLayout.addWidget(self.printUpperButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.printSetButton.setText(_translate("Dialog", "Set to be approximated"))
        self.printLowerButton.setText(_translate("Dialog", "Lower approximation"))
        self.printUpperButton.setText(_translate("Dialog", "Upper approximation"))
