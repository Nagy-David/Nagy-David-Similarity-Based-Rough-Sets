# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 796)
        MainWindow.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.534, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.points_canvas = QtWidgets.QGraphicsView(self.centralwidget)
        self.points_canvas.setGeometry(QtCore.QRect(260, 20, 611, 331))
        self.points_canvas.setStyleSheet("background-color: #FFFFFF;\n"
"border: 2px solid rgb(176, 176, 176);\n"
"")
        self.points_canvas.setObjectName("points_canvas")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(880, 20, 160, 143))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.runButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.runButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color: #333;\n"
"    border: 2px solid rgb(176, 176, 176);\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.runButton.setObjectName("runButton")
        self.verticalLayout.addWidget(self.runButton)
        self.generateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.generateButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color: #333;\n"
"    border: 2px solid rgb(176, 176, 176);\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.generateButton.setObjectName("generateButton")
        self.verticalLayout.addWidget(self.generateButton)
        self.approximateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.approximateButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color: #333;\n"
"    border: 2px solid rgb(176, 176, 176);\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.approximateButton.setObjectName("approximateButton")
        self.verticalLayout.addWidget(self.approximateButton)
        self.printApproximationButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.printApproximationButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color: #333;\n"
"    border: 2px solid rgb(176, 176, 176);\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.printApproximationButton.setObjectName("printApproximationButton")
        self.verticalLayout.addWidget(self.printApproximationButton)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 360, 291, 41))
        self.label_6.setStyleSheet(" border: 2px solid rgb(176, 176, 176);\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(30, 410, 1001, 281))
        self.table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(176, 176, 176);")
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 260, 241, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet(" background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.similarity_threshold = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.similarity_threshold.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(176, 176, 176);\n"
"")
        self.similarity_threshold.setObjectName("similarity_threshold")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.similarity_threshold)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.difference_threshold = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.difference_threshold.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(176, 176, 176);\n"
"")
        self.difference_threshold.setObjectName("difference_threshold")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.difference_threshold)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(7, 60, 251, 131))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label.setStyleSheet(" background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.x_range = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.x_range.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(176, 176, 176);\n"
"")
        self.x_range.setObjectName("x_range")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x_range)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setStyleSheet("\n"
" background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.y_range = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.y_range.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(176, 176, 176);\n"
"")
        self.y_range.setObjectName("y_range")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.y_range)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.number_of_points = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.number_of_points.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(176, 176, 176);\n"
"")
        self.number_of_points.setObjectName("number_of_points")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.number_of_points)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 20, 161, 31))
        self.label_7.setStyleSheet(" border: 2px solid rgb(176, 176, 176);\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 210, 221, 31))
        self.label_8.setStyleSheet(" border: 2px solid rgb(176, 176, 176);\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.545228, y1:0.318, x2:0.535, y2:1, stop:0 rgba(221, 220, 216, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Similarity Based Rough Sets"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.approximateButton.setText(_translate("MainWindow", "Approximate"))
        self.printApproximationButton.setText(_translate("MainWindow", "Display Approximation"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Information System</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Similarity:</span></p></body></html>"))
        self.similarity_threshold.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">50</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Difference:</span></p></body></html>"))
        self.difference_threshold.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">80</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">X-axis size:</span></p></body></html>"))
        self.x_range.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">200</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Y-axis size:</span></p></body></html>"))
        self.y_range.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">200</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Number of points:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Random Points</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Similairty thresholds</span></p></body></html>"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
