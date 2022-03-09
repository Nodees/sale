from PyQt5.QtWidgets import QWidget

from libs.functions import insert_function
from views_py.supplier import Ui_suppliers


class supplierController(QWidget, Ui_suppliers):
    def __init__(self, parent=None):
        super(supplierController, self).__init__(parent=parent)
        self.setupUi(self)

        self.on_add_supplier.clicked.connect(self.insert_method)

    def insert_method(self):
        name = self.name_supplier.text()
        document = self.document.text()

        obj = {
            'name': name,
            'legal_document': document
        }

        insert_function('supplier', obj)