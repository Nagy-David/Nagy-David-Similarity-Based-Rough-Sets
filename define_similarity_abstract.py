# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'define_similarity.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 377)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 231, 31))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 81, 21))
        self.label_5.setObjectName("label_5")
        self.difference_threshold = QtWidgets.QTextEdit(Dialog)
        self.difference_threshold.setGeometry(QtCore.QRect(100, 270, 51, 31))
        self.difference_threshold.setObjectName("difference_threshold")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 71, 21))
        self.label_4.setObjectName("label_4")
        self.similarity_threshold = QtWidgets.QTextEdit(Dialog)
        self.similarity_threshold.setGeometry(QtCore.QRect(100, 220, 51, 31))
        self.similarity_threshold.setObjectName("similarity_threshold")
        self.intervals_table = QtWidgets.QTableWidget(Dialog)
        self.intervals_table.setGeometry(QtCore.QRect(10, 110, 501, 71))
        self.intervals_table.setObjectName("intervals_table")
        self.intervals_table.setColumnCount(0)
        self.intervals_table.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 341, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 311, 16))
        self.label_3.setObjectName("label_3")
        self.applyButton = QtWidgets.QPushButton(Dialog)
        self.applyButton.setGeometry(QtCore.QRect(20, 330, 91, 23))
        self.applyButton.setObjectName("applyButton")
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(430, 70, 75, 23))
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Defining the similarity</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Difference:</span></p></body></html>"))
        self.difference_threshold.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">80</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Similarity</span></p><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.similarity_threshold.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">50</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">1. step: </span><span style=\" font-size:10pt;\">Define intervals for each attribute (if they exist)</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">2. step: </span><span style=\" font-size:10pt;\">Define similarity and difference thresholds:</span></p><p><br/></p></body></html>"))
        self.applyButton.setText(_translate("Dialog", "Apply and Exit"))
        self.saveButton.setText(_translate("Dialog", "Save"))
