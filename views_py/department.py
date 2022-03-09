# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/department.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_departments(object):
    def setupUi(self, departments):
        departments.setObjectName("departments")
        departments.resize(666, 568)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(departments)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.panel_add = QtWidgets.QWidget(departments)
        self.panel_add.setMinimumSize(QtCore.QSize(0, 120))
        self.panel_add.setMaximumSize(QtCore.QSize(16777215, 120))
        self.panel_add.setObjectName("panel_add")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.panel_add)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.title_department = QtWidgets.QLabel(self.panel_add)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title_department.setFont(font)
        self.title_department.setObjectName("title_department")
        self.verticalLayout_5.addWidget(self.title_department)
        self.label_name_department = QtWidgets.QLabel(self.panel_add)
        self.label_name_department.setObjectName("label_name_department")
        self.verticalLayout_5.addWidget(self.label_name_department)
        self.name_department = QtWidgets.QLineEdit(self.panel_add)
        self.name_department.setObjectName("name_department")
        self.verticalLayout_5.addWidget(self.name_department)
        self.on_add_department = QtWidgets.QPushButton(self.panel_add)
        self.on_add_department.setObjectName("on_add_department")
        self.verticalLayout_5.addWidget(self.on_add_department)
        self.verticalLayout_4.addWidget(self.panel_add)
        self.panel_list = QtWidgets.QWidget(departments)
        self.panel_list.setObjectName("panel_list")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.panel_list)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.list_departments = QtWidgets.QTableWidget(self.panel_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_departments.sizePolicy().hasHeightForWidth())
        self.list_departments.setSizePolicy(sizePolicy)
        self.list_departments.setMinimumSize(QtCore.QSize(0, 400))
        self.list_departments.setObjectName("list_departments")
        self.list_departments.setColumnCount(7)
        self.list_departments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_departments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_departments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_departments.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_departments.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.list_departments.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_departments.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_departments.setHorizontalHeaderItem(6, item)
        self.verticalLayout_3.addWidget(self.list_departments)
        self.verticalLayout_4.addWidget(self.panel_list)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)

        self.retranslateUi(departments)
        QtCore.QMetaObject.connectSlotsByName(departments)

    def retranslateUi(self, departments):
        _translate = QtCore.QCoreApplication.translate
        departments.setWindowTitle(_translate("departments", "Form"))
        self.title_department.setText(_translate("departments", "DEPARTMENTS LIST"))
        self.label_name_department.setText(_translate("departments", "Name:"))
        self.on_add_department.setText(_translate("departments", "Add"))
        item = self.list_departments.horizontalHeaderItem(0)
        item.setText(_translate("departments", "Id"))
        item = self.list_departments.horizontalHeaderItem(1)
        item.setText(_translate("departments", "Name"))
        item = self.list_departments.horizontalHeaderItem(2)
        item.setText(_translate("departments", "Created"))
        item = self.list_departments.horizontalHeaderItem(3)
        item.setText(_translate("departments", "Updatad"))
        item = self.list_departments.horizontalHeaderItem(4)
        item.setText(_translate("departments", "Active"))
