import sys
from PyQt5.QtWidgets import QDialog, QApplication
import numpy as np
from PyQt5 import QtWidgets

import define_similarity_abstract


class DefineSimilarity(QDialog, define_similarity_abstract.Ui_Dialog):

    def __init__(self, attributes):
        super(DefineSimilarity, self).__init__()
        self.setupUi(self)
        self.attributes = attributes
        self.intervals = []
        self.x_range = 0
        self.y_range = 0
        self.fill_table()
        self.applyButton.clicked.connect(self.accept)
        self.saveButton.clicked.connect(self.save)

        #egyelőre nem kellenek, de nem törlöm őket
        self.similarity_threshold.hide()
        self.difference_threshold.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()

    def save(self):
        for j in range(len(self.attributes)):
            if not self.intervals_table.item(0,j):
                self.intervals.append("EMPTY")
            else:
                try:
                    self.intervals.append(float(self.intervals_table.item(0,j).text()))
                except ValueError:
                    print("WRONG DATA TYPE!")
                    self.intervals.append("EMPTY")

            # self.x_range = int(self.similarity_threshold.toPlainText())
            # self.y_range = int(self.difference_threshold.toPlainText())
            # print(self.intervals)
            # print(self.x_range)
            # print(self.y_range)

    def fill_table(self):
        self.intervals_table.setColumnCount(len(self.attributes))
        self.intervals_table.setRowCount(1)

        for i, e in enumerate(self.attributes):
            item = QtWidgets.QTableWidgetItem()
            item.setText(e)
            self.intervals_table.setHorizontalHeaderItem(i, item)
