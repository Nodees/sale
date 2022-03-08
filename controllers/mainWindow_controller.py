from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QTableWidgetItem, QHeaderView

from controllers.department_controller import departmentWindowController
from controllers.stateWindow_controller import sateWindowController
from controllers.supplier_controller import supplierController
from controllers.zone_controller import zoneController
from controllers.productGroup_controller import productGroupController
from controllers.maritalStatus_controller import maritalStatusController

import models.models as model

from libs.functions import select_all, delete_function, insert_function

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
        self.widget = departmentWindowController(parent=self)
        self.body.layout().addWidget(self.widget)
        self._clear_layout_body()

        self.table = self.widget.list_departments
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items('department')

    def _on_click_actionMaritalStatus(self):
        self.widget = maritalStatusController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

    def _on_click_actionsProductGroup(self):
        self.widget = productGroupController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

    def _on_click_actionStates(self):
        self.widget = sateWindowController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

    def _on_click_actionSupplier(self):
        self.widget = supplierController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

    def _on_click_actionZone(self):
        self.widget = zoneController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

    def table_items(self, table=None):

        self.list = select_all(table)
        self.table.setRowCount(len(self.list))
        columns = len(self.list[0])

        for i, item in enumerate(self.list):
            for j, value in enumerate(item):
                content = QTableWidgetItem()
                content.setTextAlignment(4)
                content.setText(str(item[value]))

                self.table.setItem(i, j, content)

                button_delete = self._on_delete('Delete')
                button_update = self._on_update('Update')

                self.table.setCellWidget(i, columns, button_delete)
                self.table.setCellWidget(i, columns + 1, button_update)

                button_delete.clicked.connect(
                    lambda clicked, data=item['id']: self.delete_method(table, data)
                )

                button_update.clicked.connect(
                    lambda clicked, data=item: self.update_method(table, data)
                )

    @staticmethod
    def _on_delete(text_button):
        button = QPushButton()
        button.setText(text_button)
        button.setProperty('type', 'normal')

        return button

    @staticmethod
    def _on_update(text_button):
        button = QPushButton()
        button.setText(text_button)
        button.setProperty('type', 'normal')

        return button

    @staticmethod
    def delete_method(table, data: int):
        delete_function(table, data)

    @staticmethod
    def update_method(table, data: dict):
        pass

    def _clear_layout_body(self):
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()
