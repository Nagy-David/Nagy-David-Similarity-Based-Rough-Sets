# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 458)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 331, 31))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 100, 505, 321))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.num_of_base_sets_field = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.num_of_base_sets_field.setObjectName("num_of_base_sets_field")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.num_of_base_sets_field)
        self.num_of_singletons_field = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.num_of_singletons_field.setObjectName("num_of_singletons_field")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.num_of_singletons_field)
        self.avg_field = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.avg_field.setObjectName("avg_field")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.avg_field)
        self.min_field = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.min_field.setObjectName("min_field")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.min_field)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.max_field = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.max_field.setObjectName("max_field")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.max_field)
        self.stdev_field = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.stdev_field.setObjectName("stdev_field")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.stdev_field)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Descriptive Statistics</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Maximum base set size:</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Standard deviation of the base set sizes:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Average base set size:</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Number of base sets:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Number of singletons:</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Minimum base set size:</span></p></body></html>"))
