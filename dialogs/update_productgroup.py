# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/update_productgroup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_update_productgroup(object):
    def setupUi(self, update_productgroup):
        update_productgroup.setObjectName("update_productgroup")
        update_productgroup.resize(402, 183)
        self.verticalLayout = QtWidgets.QVBoxLayout(update_productgroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.confirms = QtWidgets.QWidget(update_productgroup)
        self.confirms.setObjectName("confirms")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.confirms)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputs = QtWidgets.QWidget(self.confirms)
        self.inputs.setObjectName("inputs")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.inputs)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.inputs)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.update_name = QtWidgets.QLineEdit(self.widget)
        self.update_name.setObjectName("update_name")
        self.horizontalLayout.addWidget(self.update_name)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.inputs)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.update_commission = QtWidgets.QLineEdit(self.widget_2)
        self.update_commission.setObjectName("update_commission")
        self.horizontalLayout_2.addWidget(self.update_commission)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.update_gain = QtWidgets.QLineEdit(self.widget_2)
        self.update_gain.setObjectName("update_gain")
        self.horizontalLayout_2.addWidget(self.update_gain)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.inputs)
        self.confirm_update = QtWidgets.QPushButton(self.confirms)
        self.confirm_update.setObjectName("confirm_update")
        self.verticalLayout_2.addWidget(self.confirm_update)
        self.verticalLayout.addWidget(self.confirms)

        self.retranslateUi(update_productgroup)
        QtCore.QMetaObject.connectSlotsByName(update_productgroup)

    def retranslateUi(self, update_productgroup):
        _translate = QtCore.QCoreApplication.translate
        update_productgroup.setWindowTitle(_translate("update_productgroup", "Dialog"))
        self.label.setText(_translate("update_productgroup", "Name: "))
        self.label_2.setText(_translate("update_productgroup", "Commission: "))
        self.label_3.setText(_translate("update_productgroup", "Gain: "))
        self.confirm_update.setText(_translate("update_productgroup", "Confirm"))
