from PyQt5.QtWidgets import QWidget
from views_py.maritalstatus import Ui_maritalStatus


class maritalStatusController(QWidget, Ui_maritalStatus):
    def __init__(self, parent=None):
        super(maritalStatusController, self).__init__(parent=parent)
        self.setupUi(self)
