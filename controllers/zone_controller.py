from PyQt5.QtWidgets import QWidget

from libs.functions import insert_function
from views_py.zone import Ui_zones


class zoneController(QWidget, Ui_zones):
    def __init__(self, parent=None):
        super(zoneController, self).__init__(parent=parent)
        self.setupUi(self)

        self.on_add_zone.clicked.connect(self.insert_method)

    def insert_method(self):
        name = self.name_zone.text()

        obj = {
            'name': name
        }

        insert_function('zone', obj)