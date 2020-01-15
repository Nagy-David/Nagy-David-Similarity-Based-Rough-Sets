from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
import statistics

import statistics_abstract


class StatisticsDialog(QDialog, statistics_abstract.Ui_Dialog):

    def __init__(self,singletons, base_sets):
        super(StatisticsDialog, self).__init__()
        self.setupUi(self)
        self.singletons = singletons
        self.base_sets = base_sets
        self.sizes = [len(c) for c in self.base_sets]

        self.fill()

    def fill(self):
        self.num_of_base_sets_field.setText(str(len(self.base_sets)))
        self.num_of_singletons_field.setText(str(len(self.singletons)))
        self.avg_field.setText(str(round((sum(self.sizes)/len(self.sizes)),2)))
        self.min_field.setText(str(min(self.sizes)))
        self.max_field.setText(str(max(self.sizes)))
        self.stdev_field.setText(str(round(statistics.stdev(self.sizes),2)))



