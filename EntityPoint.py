import sys
import math

from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem

class EntityPoint(QGraphicsItem):
    def __init__(self, x, y, id, attributes = None, class_value = ""):
        super(EntityPoint, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.rectF = QRectF(0, 0, 4, 4)
        self.x=x
        self.y=y
        self.id = id
        self.attributes = attributes
        self.brush = QBrush(Qt.black)
        self.pen = QPen(Qt.black)
        self.rank = 0
        self.class_value = class_value
        self.status = "normal"
        #status = {"normal","rep"}

    def setBrush(self, brush):
        self.brush = brush
        self.update()

    def boundingRect(self):
        return self.rectF

    def setBoundingRect(self,rect):
        self.rectF = rect
        self.update()

    def setPen(self,pen):
        self.pen = pen
        self.update()

    def paint(self, painter=None, style=None, widget=None):
        #painter.fillRect(self.rectF, self.brush)
        if self.status == 'normal':
            #painter.setPen(self.pen)
            self.setBoundingRect(QRectF(0, 0, 4, 4))
            painter.setBrush(self.brush)
            painter.drawEllipse(self.rectF)
        elif self.status == 'rep':
            self.setBoundingRect(QRectF(0, 0, 6, 6))
            painter.fillRect(self.rectF,self.brush)

    def __str__(self):
        return "(O{})".format(self.id)

    def distance(self, other, type):
        #type = 0 -> random point
        #type  = 1 -> dataset point
        if type == 0:
            return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))
        elif type == 1:
            s = 0
            for i in range(len(self.attributes)):
                s += (self.attributes[i]-other.attributes[i])**2
            return s**0.5


    #def distance_based_similairty(self,other):
    #    d = sum([(self.attributes[i]-other.attributes[i])**2 for i in range(len(self.attributes))])**0.5
    #
    #    return sim * 2 - 1

    def similairty(self,other,attribute_ranges):
        #ratio_list = [min(self.attributes[i],other.attributes[i])/max(self.attributes[i],other.attributes[i]) for i in range(len(self.attributes))]
        ratio_list = [abs(self.attributes[i]-other.attributes[i]) / attribute_ranges[i] for i in range(len(self.attributes))]
        ratio_list = [(-2)*v+1 for v in ratio_list]
        print("ratio: ",ratio_list)
        #sim = sum(ratio_list)/len(ratio_list)
        sim = sum(ratio_list)/len(ratio_list)
        return sim

    def __hash__(self):
        return self.id

    def __eq__(self, other):

        if isinstance(other,self.__class__) and other.id == self.id:
            return True
        return False


    def __ne__(self, other):
        return not self.__eq__(other)