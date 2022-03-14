from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QCheckBox
import controllers.controllers as controller

from libs.functions import select_all, delete_function, logical_delete_function

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
        self.widget = controller.departmentWindowController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

        self.table = self.widget.list_departments
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items('department')

    def _on_click_actionMaritalStatus(self):
        self.widget = controller.maritalStatusController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

        self.table = self.widget.list_maritalstatus
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items('marital_status')

    def _on_click_actionsProductGroup(self):
        self.widget = controller.productGroupController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

        self.table = self.widget.list_productGroups
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items('product_group')

    def _on_click_actionStates(self):
        self.widget = controller.sateWindowController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

        self.table = self.widget.list_states
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items('state')

    def _on_click_actionSupplier(self):
        self.widget = controller.supplierController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

        self.table = self.widget.list_suppliers
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items('supplier')

    def _on_click_actionZone(self):
        self.widget = controller.zoneController(parent=self)
        self._clear_layout_body()
        self.body.layout().addWidget(self.widget)

        self.table = self.widget.list_zones
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items('zone')

    def table_items(self, table=None):
        self.list = select_all(table)
        self.table.setRowCount(len(self.list))
        columns = len(self.list[0])

        for i, item in enumerate(self.list):
            for j, value in enumerate(item):
                content = QTableWidgetItem()
                checkbox = QCheckBox()

                if value == 'active':
                    checkbox.setChecked(item[value])
                    self.table.setCellWidget(i, j, checkbox)
                else:
                    content.setText(str(item[value]))

                self.table.setItem(i, j, content)

                button_delete = self._on_delete('Delete')
                button_update = self._on_update('Update')

                self.table.setCellWidget(i, columns, button_update)
                self.table.setCellWidget(i, columns + 1, button_delete)

                button_delete.clicked.connect(
                    lambda clicked, data=item['id']: self.delete_method(table, data)
                )

                button_update.clicked.connect(
                    lambda clicked, data=item: self.update_method(table, data)
                )

                checkbox.clicked.connect(
                    lambda clicked, data=item['id']: self.logical_delete_method(table, data, checkbox.isChecked())
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
    def logical_delete_method(table, data: int, status: bool):
        print(status)
        # logical_delete_function(table, data, status)

    def update_method(self, table, data: dict):

        if table == 'supplier':
            my_dialog = controller.updateSupplier(self, table, **data)
        elif table == 'state':
            my_dialog = controller.updateState(self, table, **data)
        elif table == 'product_group':
            my_dialog = controller.updateProductGroup(self, table, **data)
        else:
            my_dialog = controller.updateDepartment(self, table, **data)

        my_dialog.exec_()

    def _clear_layout_body(self):
        navigator = self.body.layout().takeAt(0)
        navigator.widget().deleteLater()
