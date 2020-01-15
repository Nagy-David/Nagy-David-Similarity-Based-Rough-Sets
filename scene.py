from PyQt5.QtGui import QPen, QBrush, QTransform
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem
from PyQt5.QtCore import pyqtSignal

import EntityPoint

class PointsGraphicsScene(QGraphicsScene):

    value_changed = pyqtSignal(int)

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(0, 0, 200, 200)
        self.count = 0
        self._item = -1

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, new_item):
        self._item = new_item
        self.value_changed.emit(new_item)

    def getPointsList(self):
        points_list = []
        for p in self.items():
            if isinstance(p, EntityPoint.EntityPoint):
                points_list.append(p)
        return points_list[::-1]

    def removeIDs(self):
        for item in self.items():
            if isinstance(item, QGraphicsTextItem):
                self.removeItem(item)

    def mousePressEvent(self, event):
        o = self.itemAt(event.scenePos(),QTransform())
        if isinstance(o, EntityPoint.EntityPoint):
            self.item = o.id





