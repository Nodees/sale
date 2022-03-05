from PyQt5.QtWidgets import QWidget
from views_py.zone import Ui_zones


class zoneController(QWidget, Ui_zones):
    def __init__(self, parent=None):
        super(zoneController, self).__init__(parent=parent)
        self.setupUi(self)
