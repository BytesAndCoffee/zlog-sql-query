# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log Explorer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1680, 1005)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 180, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 253, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nicks = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nicks.setObjectName("nicks")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nicks)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.channel = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.channel.setObjectName("channel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.datestart = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.datestart.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.datestart.setMinimumDate(QtCore.QDate(2020, 1, 1))
        self.datestart.setCalendarPopup(True)
        self.datestart.setObjectName("datestart")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.datestart)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dateend = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.dateend.setCalendarPopup(True)
        self.dateend.setObjectName("dateend")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateend)
        self.output = QtWidgets.QTableWidget(Dialog)
        self.output.setGeometry(QtCore.QRect(260, 10, 1411, 981))
        self.output.setObjectName("output")
        self.output.setColumnCount(0)
        self.output.setRowCount(0)
        self.query = QtWidgets.QPushButton(Dialog)
        self.query.setGeometry(QtCore.QRect(120, 150, 113, 32))
        self.query.setObjectName("query")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nick(s)"))
        self.label_2.setText(_translate("Dialog", "Channel"))
        self.label_3.setText(_translate("Dialog", "Start"))
        self.label_4.setText(_translate("Dialog", "End"))
        self.query.setText(_translate("Dialog", "Query"))
