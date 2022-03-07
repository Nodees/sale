from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QTableWidgetItem, QHeaderView

from controllers.department_controller import departmentWindowController
from controllers.stateWindow_controller import sateWindowController
from controllers.supplier_controller import supplierController
from controllers.zone_controller import zoneController
from controllers.productGroup_controller import productGroupController
from controllers.maritalStatus_controller import maritalStatusController

from libs.functions import select_all

from views_py.mainwindow import Ui_MainWindow


class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowController, self).__init__(parent=parent)
        self.list = None

        self.setupUi(self)

        self.actionDepartments.triggered.connect(self._on_click_actionDepartments)
        self.actionMarital_Status.triggered.connect(self._on_click_actionMaritalStatus)
        self.actionProduct_Groups.triggered.connect(self._on_click_actionsProductGroup)
        self.actionStates.triggered.connect(self._on_click_actionStates)
        self.actionSuppliers.triggered.connect(self._on_click_actionSupplier)
        self.actionZones.triggered.connect(self._on_click_actionZone)

    def _on_click_actionDepartments(self):
        widget = departmentWindowController(parent=self)
        self.body.layout().addWidget(widget)
        self._clear_layout_body()
        self.table = widget.list_departments
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items('department')

    def _on_click_actionMaritalStatus(self):
        form = maritalStatusController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(form)

    def _on_click_actionsProductGroup(self):
        widget = productGroupController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(widget)

    def _on_click_actionStates(self):
        widget = sateWindowController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(widget)

    def _on_click_actionSupplier(self):
        form = supplierController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(form)

    def _on_click_actionZone(self):
        form = zoneController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(form)

    def table_items(self, table=None):

        self.list = select_all(table)
        self.table.setRowCount(len(self.list))

        for line, value in enumerate(self.list):
            id = QTableWidgetItem()
            id.setTextAlignment(4)
            id.setText(str(value['id']))

            name = QTableWidgetItem()
            name.setTextAlignment(4)
            name.setText(str(value['name']))

            created = QTableWidgetItem()
            created.setTextAlignment(4)
            created.setText(str(value['created_at']))

            updated = QTableWidgetItem()
            updated.setTextAlignment(4)
            updated.setText(str(value['modified_at']))

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

    def _clear_layout_body(self):
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()