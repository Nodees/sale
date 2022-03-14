from datetime import datetime
from PyQt5.QtWidgets import QWidget, QDialog

from libs.functions import insert_function, update_function

from views_py.department import Ui_departments
from views_py.maritalstatus import Ui_maritalStatus
from views_py.productgroup import Ui_productGroup
from views_py.state import Ui_states
from views_py.supplier import Ui_suppliers
from views_py.zone import Ui_zones


from dialogs.update_department import Ui_Dialog
from dialogs.update_productgroup import Ui_update_productgroup
from dialogs.update_state import Ui_update_state
from dialogs.update_supplier import Ui_update_supplier


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


class sateWindowController(QWidget, Ui_states):
    def __init__(self, parent=None):
        super(sateWindowController, self).__init__(parent=parent)
        self.setupUi(self)

        self.on_add_state.clicked.connect(self.insert_method)

    def insert_method(self):
        name = self.name_state.text()
        abbreviation = self.abbreviation.text()

        obj = {
            'name': name,
            'abbreviation': abbreviation
        }

        insert_function('state', obj)


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


class updateDepartment(QDialog, Ui_Dialog):
    def __init__(self, parent=None, table=None, **kwargs):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.data = kwargs
        self.table = table

        self.update_name.setText(kwargs.get('name'))

        self.confirm_update.clicked.connect(self.update_method)

    def update_method(self):
        name = self.update_name.text()
        update_at = datetime.now()

        self.data.update({'name': name})
        self.data.update({'modified_at': update_at})

        update_function(self.table, self.data)


class updateProductGroup(QDialog, Ui_update_productgroup):
    def __init__(self, parent=None, table=None, **kwargs):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.data = kwargs
        self.table = table

        self.update_name.setText(kwargs.get('name'))
        self.update_commission.setText(str(kwargs.get('commission_percentage')))
        self.update_gain.setText(str(kwargs.get('gain_percentage')))

        self.confirm_update.clicked.connect(self.update_method)

    def update_method(self):
        name = self.update_name.text()
        commission_percentage = self.update_commission.text()
        gain_percentage = self.update_gain.text()
        update_at = datetime.now()

        self.data.update({'name': name})
        self.data.update({'commission_percentage': commission_percentage})
        self.data.update({'gain_percentage': gain_percentage})
        self.data.update({'modified_at': update_at})

        update_function(self.table, self.data)


class updateState(QDialog, Ui_update_state):
    def __init__(self, parent=None, table=None, **kwargs):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.data = kwargs
        self.table = table

        self.update_name.setText(kwargs.get('name'))
        self.update_abbreviation.setText(kwargs.get('abbreviation'))

        self.confirm_update.clicked.connect(self.update_method)

    def update_method(self):
        name = self.update_name.text()
        abbreviation = self.update_abbreviation.text()
        update_at = datetime.now()

        self.data.update({'name': name})
        self.data.update({'abbreviation': abbreviation})
        self.data.update({'modified_at': update_at})

        update_function(self.table, self.data)


class updateSupplier(QDialog, Ui_update_supplier):
    def __init__(self, parent=None, table=None, **kwargs):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.data = kwargs
        self.table = table

        self.update_name.setText(kwargs.get('name'))
        self.update_document.setText(kwargs.get('legal_document'))

        self.confirm_update.clicked.connect(self.update_method)

    def update_method(self):
        name = self.update_name.text()
        legal_document = self.update_document.text()
        update_at = datetime.now()

        self.data.update({'name': name})
        self.data.update({'legal_document': legal_document})
        self.data.update({'modified_at': update_at})

        update_function(self.table, self.data)
