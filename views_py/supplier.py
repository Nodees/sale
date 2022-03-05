# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/supplier.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_suppliers(object):
    def setupUi(self, suppliers):
        suppliers.setObjectName("suppliers")
        suppliers.resize(617, 368)
        self.verticalLayout = QtWidgets.QVBoxLayout(suppliers)
        self.verticalLayout.setObjectName("verticalLayout")
        self.panel_add = QtWidgets.QWidget(suppliers)
        self.panel_add.setMinimumSize(QtCore.QSize(0, 120))
        self.panel_add.setMaximumSize(QtCore.QSize(16777215, 120))
        self.panel_add.setObjectName("panel_add")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.panel_add)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.title_supplier = QtWidgets.QLabel(self.panel_add)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title_supplier.setFont(font)
        self.title_supplier.setObjectName("title_supplier")
        self.verticalLayout_5.addWidget(self.title_supplier)
        self.label_name_supplier = QtWidgets.QLabel(self.panel_add)
        self.label_name_supplier.setObjectName("label_name_supplier")
        self.verticalLayout_5.addWidget(self.label_name_supplier)
        self.name_supplier = QtWidgets.QLineEdit(self.panel_add)
        self.name_supplier.setObjectName("name_supplier")
        self.verticalLayout_5.addWidget(self.name_supplier)
        self.on_add_supplier = QtWidgets.QPushButton(self.panel_add)
        self.on_add_supplier.setObjectName("on_add_supplier")
        self.verticalLayout_5.addWidget(self.on_add_supplier)
        self.verticalLayout.addWidget(self.panel_add)
        self.panel_list = QtWidgets.QWidget(suppliers)
        self.panel_list.setObjectName("panel_list")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.panel_list)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.list_suppliers = QtWidgets.QTableWidget(self.panel_list)
        self.list_suppliers.setMinimumSize(QtCore.QSize(0, 200))
        self.list_suppliers.setMaximumSize(QtCore.QSize(720, 200))
        self.list_suppliers.setObjectName("list_suppliers")
        self.list_suppliers.setColumnCount(5)
        self.list_suppliers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_suppliers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_suppliers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_suppliers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_suppliers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_suppliers.setHorizontalHeaderItem(4, item)
        self.list_suppliers.horizontalHeader().setCascadingSectionResizes(True)
        self.list_suppliers.horizontalHeader().setDefaultSectionSize(112)
        self.list_suppliers.horizontalHeader().setSortIndicatorShown(False)
        self.list_suppliers.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.list_suppliers)
        self.verticalLayout.addWidget(self.panel_list)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(suppliers)
        QtCore.QMetaObject.connectSlotsByName(suppliers)

    def retranslateUi(self, suppliers):
        _translate = QtCore.QCoreApplication.translate
        suppliers.setWindowTitle(_translate("suppliers", "Form"))
        self.title_supplier.setText(_translate("suppliers", "SUPLIERSS LIST"))
        self.label_name_supplier.setText(_translate("suppliers", "Name:"))
        self.on_add_supplier.setText(_translate("suppliers", "Add"))
        item = self.list_suppliers.horizontalHeaderItem(0)
        item.setText(_translate("suppliers", "Id"))
        item = self.list_suppliers.horizontalHeaderItem(1)
        item.setText(_translate("suppliers", "Name"))
        item = self.list_suppliers.horizontalHeaderItem(2)
        item.setText(_translate("suppliers", "Document"))
        item = self.list_suppliers.horizontalHeaderItem(3)
        item.setText(_translate("suppliers", "Created"))
        item = self.list_suppliers.horizontalHeaderItem(4)
        item.setText(_translate("suppliers", "Update"))
