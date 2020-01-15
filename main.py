import pathlib
import sys

import numpy as np
import random
import pandas as pd

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTime, QDate, QLine, QRectF, pyqtSignal, QUrl
from PyQt5.QtGui import QColor, QPen, QBrush, QIcon
from PyQt5.QtWidgets import QAction, QFileDialog, QGraphicsTextItem, QDialog, QMessageBox, QInputDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView

import os
import statistics_dialog
import EntityPoint
import groups as gr
import UnionFindA
from annotation import Annotation
from approximation_dialog import Approximation
from contractdict import ContractDict2
import main_window
import scene
import rank as r
import define_similarity


# import QtGui.QStyle

class MainMenu(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    count = 0  # number of objects

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.setupUi(self)

        self.generateButton.clicked.connect(self.generate)
        self.approximateButton.clicked.connect(self.approximate)
        self.runButton.clicked.connect(self.run)
        self.printApproximationButton.clicked.connect(self.printApproximation)

        @pyqtSlot(int)
        def selectItem(index):
            self.table.selectRow(index)

        self.points_canvas.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.points_canvas.scene = scene.PointsGraphicsScene()
        self.points_canvas.setScene(self.points_canvas.scene)

        self.points_canvas.scene.value_changed.connect(selectItem)

        self.points_type = 0
        self.points_list = []
        self.colors = []
        self.attributes = []
        self.attribute_intervals = []
        self.headers = []
        self.attribute_ranges = []

        self.set_to_be_approximated = set()

        self.clusters = []
        self.singletons = []
        self.representatives = []

        self.accuracy_clustering = []
        self.base_sets_clustering = []
        self.lower_approximaton_clustering = []
        self.upper_approximaton_clustering = []

        openFile = QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        setAnnotation = QAction('&Set Annotation', self)
        setAnnotation.setShortcut('Ctrl+N')
        setAnnotation.setStatusTip('Set Annotation')
        setAnnotation.triggered.connect(self.set_annotation)

        defineSimilarity = QAction('&Define Similarity', self)
        defineSimilarity.setShortcut('Ctrl+M')
        defineSimilarity.setStatusTip('Define Similarity')
        defineSimilarity.triggered.connect(self.define_simmilarity_dialog)

        printStatistics = QAction('&Statistics', self)
        printStatistics.setShortcut('Ctrl+S')
        printStatistics.setStatusTip('Statistics')
        printStatistics.triggered.connect(self.print_statistics)

        loadRandomPoints = QAction('&Load Random Points', self)
        loadRandomPoints.setShortcut('Ctrl+L')
        loadRandomPoints.setStatusTip('Load Random Points')
        loadRandomPoints.triggered.connect(self.load_random_points)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(setAnnotation)
        fileMenu.addAction(defineSimilarity)
        fileMenu.addAction(printStatistics)
        fileMenu.addAction(loadRandomPoints)

        about = QAction('&About', self)
        about.setStatusTip('About')
        about.triggered.connect(self.displayHelp)

        helpMenu = mainMenu.addMenu('&Help')
        helpMenu.addAction(about)

        iconPath = "./UI files/icons/"
        self.display_id = False
        # Toolbar actions

        # loadRandomPointsToolBar = QAction(self.style().standardIcon(QtGui.QStyle.SP_DialogOpenButton), 'Load Points', self)
        # loadRandomPointsToolBar.triggered.connect(self.load_random_points)
        printOriginalPointsToolBar = QAction(QIcon(iconPath + "points_icon.jpg"), 'Display Points', self)
        printOriginalPointsToolBar.triggered.connect(self.printOriginalPoints)
        printBaseSetsToolBar = QAction(QIcon(iconPath + "base_sets_icon.jpg"), 'Display Base Sets', self)
        printBaseSetsToolBar.triggered.connect(self.colorClustersClustering)
        printRepresentativesToolBar = QAction(QIcon(iconPath + "icons_representatives.jpg"), 'Display Representatives',
                                              self)
        printRepresentativesToolBar.triggered.connect(self.displayRepresentatives)
        printIDToolBar = QAction(QIcon(iconPath + "id_icon.jpg"), 'Display IDs', self)
        printIDToolBar.triggered.connect(self.displayID)

        # self.toolBar = self.addToolBar("LoadPoints")
        # self.toolBar.addAction(loadRandomPointsToolBar)
        self.toolBar.addAction(printOriginalPointsToolBar)
        self.toolBar.addAction(printBaseSetsToolBar)
        self.toolBar.addAction(printRepresentativesToolBar)
        self.toolBar.addAction(printIDToolBar)

    # -------------------------------------------------------------------------------------------------------------------
    def displayHelp(self):
        global web
        web = QWebView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Html/main_help.html"))
        local_url = QUrl.fromLocalFile(file_path)
        web.load(local_url)
        web.show()

    """Read a csv file containing objects. There is a possibility to normalize the given data.
    Points are given to the canvas. 
    """

    def file_open(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        if not name:
            return

        self.points_type = 1

        x = int(self.x_range.toPlainText())
        y = int(self.y_range.toPlainText())

        df = pd.read_csv(name, header=0)
        df = df.replace('NaN', np.NaN)

        while True:

            num, ok = QInputDialog.getInt(self,
                                          "Index of the class attribute in the Information System. Type -1 if there is no class attribute.",
                                          "The index of the decision attribue:")
            if ok:
                dec_attr_index = num
                if not (dec_attr_index in range(0, len(df.columns)) or dec_attr_index == -1):
                    QMessageBox.about(self, "Error!", "There is no column with such an index!")
                else:
                    break

        self.headers = list(df.columns.values)
        class_values = []

        # if there is a class label attribute, then it will be removed
        if dec_attr_index != -1:
            dec_attr_list = df[df.columns[dec_attr_index]].tolist()
            df.drop(df.columns[dec_attr_index], axis=1, inplace=True)
            class_values = pd.Series(dec_attr_list)

        # for each column we compute the max and the min value
        for i in range(len(df.columns)):
            max = df[df.columns[i]].dropna().max()
            min = df[df.columns[i]].dropna().min()
            self.attribute_ranges.append(max - min)

        # normalization
        msg = "Would you like to normalize the data?"
        reply = QMessageBox.question(self, 'Message', msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            for i in range(len(df.columns)):
                df[df.columns[i]] = df[df.columns[i]].apply(lambda x: (x - min) / (max - min))

        else:
            pass

        # create points on canvas (randomly)
        for i in range(0, len(df.values)):
            r1 = random.randint(0, x + 1)
            r2 = random.randint(0, y + 1)

            # if there is a class label attribute, then its value will be added to each point
            if dec_attr_index != -1:
                entity = EntityPoint.EntityPoint(r1, r2, self.count, df.values[i], class_values[i])
            else:
                entity = EntityPoint.EntityPoint(r1, r2, self.count, df.values[i])

            # if  "nan" in df.values[i]:
            #     entity.has_missing = True

            entity.setPos(r1, r2)
            self.count += 1
            self.points_canvas.scene.addItem(entity)

        # a flag for class label attribute
        has_decision_attributes = len(class_values) != 0

        self.fill_table(self.headers, has_decision_attributes)
        self.generateButton.setEnabled(False)
        self.similarity_threshold.setEnabled(False)
        self.difference_threshold.setEnabled(False)
        self.number_of_points.setEnabled(False)

    # -------------------------------------------------------------------------------------------------------------------
    """Fills the table with the information read from a csv file"""

    def fill_table(self, headers, has_decision_attributes):
        self.table.setColumnCount(len(headers))
        self.table.setRowCount(self.count)

        points = self.points_canvas.scene.getPointsList()

        for i, e in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            item.setText(e)
            self.table.setHorizontalHeaderItem(i, item)

        if not has_decision_attributes:
            for i, e in enumerate(points):
                for j in range(len(headers)):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(e.attributes[j]))
                    self.table.setItem(i, j, item)
        # if there is a class label attribute, then it will be added as the last column
        else:
            for i, e in enumerate(points):
                for j in range(len(headers) - 1):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(e.attributes[j]))
                    self.table.setItem(i, j, item)
            for i, e in enumerate(points):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(e.class_value))
                self.table.setItem(i, len(headers) - 1, item)

    def fill_table_random_points(self):
        points = self.points_canvas.scene.getPointsList()
        self.table.setColumnCount(2)
        self.table.setRowCount(self.count)
        self.table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("X"))
        self.table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Y"))

        for i, e in enumerate(points):
            item_x = QtWidgets.QTableWidgetItem()
            item_x.setText(str(e.x))
            self.table.setItem(i, 1, item_x)
            item_y = QtWidgets.QTableWidgetItem()
            item_y.setText(str(e.y))
            self.table.setItem(i, 2, item_y)

    # -------------------------------------------------------------------------------------------------------------------
    "Load previously generated random points from a csv file"

    def load_random_points(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        df = pd.read_csv(name, header=0)
        for v in df.values:
            entity = EntityPoint.EntityPoint(int(v[1]), int(v[2]), self.count)
            entity.setPos(int(v[1]), int(v[2]))
            self.count += 1
            self.points_canvas.scene.addItem(entity)

    "Print the points with black on the canvas"

    def printOriginalPoints(self):
        for item in self.points_canvas.scene.items():
            if isinstance(item, EntityPoint.EntityPoint):
                item.status = "normal"
                item.setBrush(Qt.black)

    "Print the points with the corresponding cluster color"

    def colorClustersClustering(self):
        self.colorClusters(self.base_sets_clustering)

    """
    Displays the representative members as a larger rectangle
    """

    def displayRepresentatives(self):
        self.colorClusters(self.base_sets_clustering)
        for rep in self.representatives:
            for item in self.points_canvas.scene.items():
                if isinstance(item, EntityPoint.EntityPoint):
                    if rep.id == item.id:
                        item.status = "rep"
                        item.update()

    """
    Display object ID (point ID)
    """

    def displayID(self):
        if not self.display_id:
            for item in self.points_canvas.scene.items():
                if isinstance(item, EntityPoint.EntityPoint):
                    text = QGraphicsTextItem(str(item.id))
                    text.setPos(item.x + 2, item.y - 2)
                    self.points_canvas.scene.addItem(text)
            self.display_id = True
        else:
            self.points_canvas.scene.removeIDs()
            self.display_id = False

    "Print the set to be approximated with green, the lower (red), and the upper approximation (blue)"

    def printApproximation(self):
        dialog = Approximation(self.points_list[::], self.set_to_be_approximated.copy(),
                               self.lower_approximaton_clustering[::], self.upper_approximaton_clustering[::])

        if dialog.exec_() == QDialog.Accepted:
            print("Display Approximation")
        else:
            print('Cancelled')
        dialog.deleteLater()

    "Opens the statistics dialog"

    def print_statistics(self):
        dialog = statistics_dialog.StatisticsDialog(self.singletons, self.base_sets_clustering)
        if dialog.exec_() == QDialog.Accepted:
            pass
        else:
            pass
        dialog.deleteLater()

    "Sets the annotation process"

    def set_annotation(self):
        dialog = Annotation(self.singletons, self.base_sets_clustering, self.representatives, self.points_type)
        if dialog.exec_() == QDialog.Accepted:
            self.base_sets_clustering = dialog.base_sets
            self.colorClusters(self.base_sets_clustering)
        else:
            print('Cancelled')
        dialog.deleteLater()

    """
    Defines the cluster colors
    """

    def colorClusters(self, points):
        step = 400 / len(points) - 1
        for i in range(0, 400, int(step)):
            color = QColor.fromHsv(i, 255, 255)
            self.colors.append(color)

        for i, c in enumerate(points):
            for element in c:
                for item in self.points_canvas.scene.items():
                    if isinstance(item, EntityPoint.EntityPoint):
                        if element.id == item.id:
                            item.status = "normal"
                            item.setBrush(self.colors[i])

    """
    Defines the clusters, the representative members for each cluster and the system of base sets
    """

    def printClusters(self):
        clusters_all = self.getClusters()
        self.clusters = [c for c in clusters_all if len(c) != 0]
        self.representatives = r.getRepresentatives(self.clusters)
        self.getBaseSets()

    """
    Returns the clusters generated by the correlation clustering.
    One cluster is a list of lists.
    """

    def getClusters(self):
        size = len(self.best[0])
        clusters = [[] for _ in range(size)]
        for i in range(size):
            j = self.best[0][i]
            clusters[j].append(self.points_list[i])
        return clusters

    """
    Defines the system of base sets. 
    A base set is a cluster whose cardinality is more than 1.
    """

    def getBaseSets(self):
        self.singletons = [c for c in self.clusters if len(c) == 1]
        self.base_sets_clustering = [set(c) for c in self.clusters if len(c) > 1]
        print("Base sets using correlation clustering using: ")
        for c in self.base_sets_clustering:
            print([str(item) for item in c])
            print()

        print("Singletons:")
        print([str(item[0]) for item in self.singletons])

    """Generates random points in the canvas"""

    def generate(self):
        x = int(self.x_range.toPlainText())
        y = int(self.y_range.toPlainText())
        n = int(self.number_of_points.toPlainText())

        time = QTime.currentTime()
        now = QDate.currentDate()
        s = str(now.year()) + "_" + str(now.month()) + "_" + str(now.day()) + "_" + str(time.hour()) + "_" + str(
            time.minute()) + "_" + str(time.second())

        pathlib.Path('Input\\RandomPoints\\').mkdir(parents=True, exist_ok=True)
        path = "Input\\RandomPoints\\random_points_" + s + ".csv"
        with open(path, 'w') as file:
            for i in range(0, n):
                r1 = random.randint(0, x + 1)
                r2 = random.randint(0, y + 1)
                file.write(str(self.count) + "," + str(r1) + "," + str(r2) + "\n")

                if self.points_type == 0:
                    entity = EntityPoint.EntityPoint(r1, r2, self.count)

                entity.setPos(r1, r2)
                self.count += 1
                self.points_canvas.scene.addItem(entity)

            self.fill_table_random_points()

    # -------------------------------------------------------------------------------------------------------------------
    """
    Defines the lower and upper approximation and the accuracy of the approximation
    """

    def approximate(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter the points to be approximated:')
        if ok:
            interval = text.split("-")
            points_to_be_approximated = [self.points_list[i] for i in range(int(interval[0]), int(interval[1]) + 1)]

            self.set_to_be_approximated = set(points_to_be_approximated)

            print("The set to be approximated")
            print([item for item in self.set_to_be_approximated])

            for bs in self.base_sets_clustering:

                if bs.issubset(self.set_to_be_approximated):
                    self.lower_approximaton_clustering.append(bs)
                if bool(bs.intersection(self.set_to_be_approximated)):
                    self.upper_approximaton_clustering.append(bs)

            print("Lower approximation using correlation clustering: ")
            for bs in self.lower_approximaton_clustering:
                print([str(item) for item in bs])
                print()
            print("--------------------------")
            print("Upper approximation using correlation clustering: ")
            for bs in self.upper_approximaton_clustering:
                print([str(item) for item in bs])
                print()
            print("--------------------------")

            card_lower_cl = sum([len(l) for l in self.lower_approximaton_clustering])
            card_upper_cl = sum([len(l) for l in self.upper_approximaton_clustering])
            accuracy = card_lower_cl / card_upper_cl
            print("Accuracy of the approximation: ", accuracy)

    """Define similarity using a dialog"""

    def define_simmilarity_dialog(self):
        dialog = define_similarity.DefineSimilarity(self.headers)
        if dialog.exec_() == QDialog.Accepted:
            self.attribute_intervals = dialog.intervals
            print("Intervals: ", self.attribute_intervals)
        else:
            pass
        dialog.deleteLater()

    """"""

    def too_high_difference(self, i, j):
        for k in range(1, len(self.attribute_intervals)):
            if self.attribute_intervals[k] != 'EMPTY':
                if abs(self.points_list[i].attributes[k] - self.points_list[j].attributes[k]) >= self.attribute_intervals[k]:
                    return True
        return False

    """Defines similarity"""
    def define_simmilarity_rel(self):
        simm = float(self.similarity_threshold.toPlainText())
        diff = float(self.difference_threshold.toPlainText())
        self.points_list = self.points_canvas.scene.getPointsList()
        num_of_points = len(self.points_list)
        relation = np.zeros((num_of_points, num_of_points))

        # max_d = -1
        # min_d = np.inf
        # for i in range(num_of_points):
        #     for j in range(i+1,num_of_points):
        #         d = self.points_list[i].distance(self.points_list[j], self.points_type)
        #         if d < min_d:
        #             min_d = d
        #         if d > max_d:
        #             max_d = d

        for i in range(num_of_points):
            for j in range(i + 1, num_of_points):

                # continous data
                if self.points_type == 1:
                    d = self.points_list[i].distance(self.points_list[j], self.points_type)
                    if np.isnan(d) or self.too_high_difference(i, j):
                        sim = -1
                    else:
                        # jó: 0.8 és 2
                        if d < 0.6:
                            sim = 1
                        elif d > 1.5:
                            sim = -1
                        else:
                            # f(t) = c+((d-c)/(b-a))*(t-a)
                            a = 1
                            b = 2
                            c = -1
                            d = 1
                            sim = c + ((d - c) / (b - a)) * (d - a)
                    relation[i][j] = sim
                    relation[j][i] = sim

                # random points
                else:
                    d = self.points_list[i].distance(self.points_list[j], self.points_type)
                    if d > diff or np.isnan(d):
                        relation[i][j] = -1
                        relation[j][i] = -1
                    elif d <= simm:
                        relation[i][j] = 1
                        relation[j][i] = 1
                    else:
                        relation[i][j] = 0
                        relation[j][i] = 0

        return relation

    """
    Defines the similarity relation and runs the contraction method.
    """

    def run(self):
        self.relation = self.define_simmilarity_rel()
        rows, columns = self.relation.shape

        graph = []

        for i in range(0, rows):
            for j in range(0, rows):
                graph.append((i, j, self.relation[i][j]))

        uf = UnionFindA.UnionFind(rows)
        c = ContractDict2(rows, graph)
        c.contract(uf, 0, rows)

        fc = gr.calculate(uf.array, self.relation, rows)
        self.best = (uf.array, fc)

        self.printClusters()
        self.colorClusters(self.base_sets_clustering)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = MainMenu()
    form.show()
    sys.exit(app.exec_())
