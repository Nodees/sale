from PyQt5.QtWidgets import QWidget

from libs.functions import insert_function
from views_py.productgroup import Ui_productGroup


class productGroupController(QWidget, Ui_productGroup):
    def __init__(self, parent=None):
        super(productGroupController, self).__init__(parent=parent)
        self.setupUi(self)

        self.on_add_productGroup.clicked.connect(self.insert_method)

    def insert_method(self):
        name = self.name_productGroup.text()
        commission = self.commission.text()
        gain = self.gain.text()


        obj = {
            'name': str(name),
            'commission_percentage': str(commission),
            'gain_percentage': str(gain)
        }

        insert_function('product_group', obj)