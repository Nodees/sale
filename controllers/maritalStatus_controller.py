from PyQt5.QtWidgets import QWidget

from libs.functions import insert_function
from views_py.maritalstatus import Ui_maritalStatus


class maritalStatusController(QWidget, Ui_maritalStatus):
    def __init__(self, parent=None):
        super(maritalStatusController, self).__init__(parent=parent)
        self.setupUi(self)

        self.on_add_maritalstatus.clicked.connect(self.insert_method)

    def insert_method(self):
        name = self.name_maritalstatus.text()

        obj = {
            'name': str(name)
        }

        insert_function('marital_status', obj)