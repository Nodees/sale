from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QTableWidgetItem

from controllers.departmentController import departmentWindowController
from controllers.stateWindowController import sateWindowController
from controllers.supplierController import supplierController
from controllers.zoneController import zoneController
from controllers.productGroupController import productGroupController
from controllers.maritalStatusController import maritalStatusController

from libs.functions import _list

from views_py.mainwindow import Ui_MainWindow


class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowController, self).__init__(parent=parent)
        self.setupUi(self)
        self.actionDepartments.triggered.connect(self._on_click_actionDepartments)
        self.actionMarital_Status.triggered.connect(self._on_click_actionMaritalStatus)
        self.actionProduct_Groups.triggered.connect(self._on_click_actionsProductGroup)
        self.actionStates.triggered.connect(self._on_click_actionStates)
        self.actionSuppliers.triggered.connect(self._on_click_actionSupplier)
        self.actionZones.triggered.connect(self._on_click_actionZone)

    def _on_click_actionDepartments(self):
        widget = departmentWindowController(parent=self)
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()
        self.body.layout().addWidget(widget)

        self.table = widget.list_departments
        self.table_items()

    def _on_click_actionMaritalStatus(self):
        form = maritalStatusController(parent=self)
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()
        self.body.layout().addWidget(form)

    def _on_click_actionsProductGroup(self):
        widget = productGroupController(parent=self)
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()
        self.body.layout().addWidget(widget)

    def _on_click_actionStates(self):
        widget = sateWindowController(parent=self)
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()
        self.body.layout().addWidget(widget)

    def _on_click_actionSupplier(self):
        form = supplierController(parent=self)
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()
        self.body.layout().addWidget(form)

    def _on_click_actionZone(self):
        form = zoneController(parent=self)
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()
        self.body.layout().addWidget(form)

    def table_items(self):

        self.list = _list()
        self.table.setRowCount(len(self.list))

        for line, valor in enumerate(self.list):
            id = QTableWidgetItem()
            id.setTextAlignment(4)
            id.setText(str(valor[0]))

            name = QTableWidgetItem()
            name.setTextAlignment(4)
            name.setText(str(valor[1]))

            created = QTableWidgetItem()
            created.setTextAlignment(4)
            created.setText(str(valor[2]))

            updated = QTableWidgetItem()
            updated.setTextAlignment(4)
            updated.setText(str(valor[3]))

            button_delete = self._on_delete('Delete')
            button_update = self._on_update('Update')

            self.table.setItem(line, 0, id)
            self.table.setItem(line, 1, name)
            self.table.setItem(line, 2, created)
            self.table.setItem(line, 3, updated)
            self.table.setCellWidget(line, 4, button_delete)
            self.table.setCellWidget(line, 5, button_update)

    def _on_delete(self, text_button):
        button = QPushButton()
        button.setText(text_button)
        button.setProperty('type', 'normal')

        return button

    def _on_update(self, text_button):
        button = QPushButton()
        button.setText(text_button)
        button.setProperty('type', 'normal')

        return button
