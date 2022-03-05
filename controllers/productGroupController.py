from PyQt5.QtWidgets import QWidget
from views_py.productgroup import Ui_productGroup


class productGroupController(QWidget, Ui_productGroup):
    def __init__(self, parent=None):
        super(productGroupController, self).__init__(parent=parent)
        self.setupUi(self)
