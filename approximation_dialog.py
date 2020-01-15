from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene, QGraphicsItem

import EntityPoint
import approximation_abstract


class Approximation(QDialog, approximation_abstract.Ui_Dialog):
    def __init__(self, points, set, lower, upper):
        super(Approximation, self).__init__()
        self.setupUi(self)

        self.points = points
        self.set = set
        self.lower = lower
        self.upper = upper
        self.points_canvas.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.points_canvas.scene = QGraphicsScene()
        self.points_canvas.setScene(self.points_canvas.scene)

        self.printLowerButton.clicked.connect(self.printLowerApproximation)
        self.printUpperButton.clicked.connect(self.printUpperApproximation)
        self.printSetButton.clicked.connect(self.printSet)
        self.okButton.clicked.connect(self.accept)

        path = "./Output/Approximation/"
        self.writeLowerApproximationFile(path+'lower_approximation_clustering.txt')
        self.writeUpperApproximationFile(path+'upper_approximation_clustering.txt')
        self.writeSetFile(path+'set_to_be_approximated_clustering.txt')

        self.displayOriginalPoints()

    def displayOriginalPoints(self):
        for e in self.points:
            self.points_canvas.scene.addEllipse(QRectF(e.x, e.y, 4, 4), QPen(Qt.black), QBrush(Qt.black))

    def printLowerApproximation(self):
        self.displayOriginalPoints()
        base_sets = [list(c) for c in self.lower]
        for i in range(len(base_sets)):
            for e in base_sets[i]:
                self.points_canvas.scene.addEllipse(QRectF(e.x, e.y, 4, 4), QPen(Qt.red), QBrush(Qt.red))

    def printUpperApproximation(self):
        self.displayOriginalPoints()
        base_sets = [list(c) for c in self.upper]
        for c in base_sets:
            for e in c:
                self.points_canvas.scene.addEllipse(QRectF(e.x, e.y, 4, 4), QPen(Qt.blue), QBrush(Qt.blue))

    def printSet(self):
        self.displayOriginalPoints()
        base_sets = list(self.set)
        for e in base_sets:
            self.points_canvas.scene.addEllipse(QRectF(e.x, e.y, 4, 4), QPen(Qt.green), QBrush(Qt.green))

    def writeLowerApproximationFile(self,fname):
        with open(fname, 'w') as file:
            points_set = set(self.points)
            lower_list = []
            for b in self.lower:
                lower_list += list(b)
            lower_set = set(lower_list)
            lower_complement = points_set.difference(lower_set)

            for e in list(lower_complement):
                s = str(e.x)+" "+str(e.y)+" "+str(3)+'\n'
                file.write(s)

            for e in list(lower_set):
                s = str(e.x) + " " + str(e.y) + " " + str(0)+'\n'
                file.write(s)


    def writeUpperApproximationFile(self,fname):
        with open(fname, 'w') as file:
            points_set = set(self.points)
            upper_list = []
            for b in self.upper:
                upper_list += list(b)
            upper_set = set(upper_list)
            upper_complement = points_set.difference(upper_set)

            for e in list(upper_complement):
                s = str(e.x) + " " + str(e.y) + " " + str(3) + '\n'
                file.write(s)

            for e in list(upper_set):
                s = str(e.x) + " " + str(e.y) + " " + str(0) + '\n'
                file.write(s)


    def writeSetFile(self,fname):
        with open(fname, 'w') as file:

            points_set = set(self.points)
            set_complement = points_set.difference(self.set)
            for e in list(set_complement):
                s = str(e.x)+" "+str(e.y)+" "+str(3)+'\n'
                file.write(s)

            for e in list(self.set):
                s = str(e.x) + " " + str(e.y) + " " + str(0)+'\n'
                file.write(s)

