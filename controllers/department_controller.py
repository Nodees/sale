from PyQt5.QtWidgets import QWidget

from libs.functions import insert_function
from views_py.department import Ui_departments
import models.models as model


class departmentWindowController(QWidget, Ui_departments):
    def __init__(self, parent=None):
        super(departmentWindowController, self).__init__(parent=parent)
        self.setupUi(self)

        self.on_add_department.clicked.connect(self.insert_method)

    def insert_method(self):
        name = self.name_department.text()

        obj = {
            'name': str(name)
        }

        insert_function('department', obj)