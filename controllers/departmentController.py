from PyQt5.QtWidgets import QWidget
from views_py.department import Ui_departments


class departmentWindowController(QWidget, Ui_departments):
    def __init__(self, parent=None):
        super(departmentWindowController, self).__init__(parent=parent)
        self.setupUi(self)
