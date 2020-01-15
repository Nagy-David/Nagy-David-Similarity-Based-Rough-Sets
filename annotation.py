import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QMessageBox

import annotation_abstract
import representant as rep


class Annotation(QDialog, annotation_abstract.Ui_Dialog):

    def __init__(self,singletons,base_sets,representants,points_type):
        super(Annotation, self).__init__()
        self.setupUi(self)
        self.singletons = singletons
        self.base_sets = base_sets
        self.representants = representants

        self.applyButton.clicked.connect(self.accept)
        self.insertButton.clicked.connect(self.insertSingleton)
        self.helpButton.clicked.connect(self.findClosest)
        self.points_type = points_type


        self.listOfBaseSets.append("Base sets using correlation clustering: ")

        for c in self.base_sets:
            self.listOfBaseSets.append(' '.join([str(item.id) for item in c]))
            self.listOfBaseSets.append('')

        for item in self.singletons:
            self.listOfSingletons.addItem(str(item[0]))

        for i in range(0,len(self.base_sets)):
            self.listOfClusterIDs.addItem(str(i))

        # print("Singletons:")
        # for item in self.singletons:
        #     print(str(item[0]))
        #     print("closest cluster: ",rep.closestRepresentant(self.representants,item[0]))

    def findClosest(self):
        s_id = int(self.singleton_id.toPlainText())
        for i in range(0,len(self.singletons)):
            if self.singletons[i][0].id == s_id:
                index = i
                break
        nearest = rep.closestRepresentant(self.representants, self.singletons[index][0],self.points_type)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        s = "The nearest cluster for the selected singleton is: "+ str(nearest)
        msg.setText(s)
        msg.setWindowTitle("Nearest cluster")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.msgbtn)
        msg.exec_()

    def msgbtn(self):
        print("Button pressed is:")


    def insertSingleton(self):
        s_id = int(self.singleton_id .toPlainText())
        c_id = int(self.cluster_id .toPlainText())

        for i in range(0,len(self.singletons)):
            if self.singletons[i][0].id == s_id:
                index = i
                break

        self.base_sets[c_id].add(self.singletons[index][0])
        self.listOfSingletons.takeItem(index)
        del self.singletons[index]


        print(("Base sets using correlation clustering with annotation: "))
        for c in self.base_sets:
            print(' '.join([str(item.id) for item in c]))

        print("Singletons:")
        for item in self.singletons:
            print(str(item[0]))

#
# app = QApplication(sys.argv)
# dialog = Annotation([],[])
# dialog.show()
# app.exec_()