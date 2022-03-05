from PyQt5.QtWidgets import QWidget
from views_py.supplier import Ui_suppliers


class supplierController(QWidget, Ui_suppliers):
    def __init__(self, parent=None):
        super(supplierController, self).__init__(parent=parent)
        self.setupUi(self)
