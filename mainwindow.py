# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.silenceModeLabel = QtWidgets.QLabel(self.centralWidget)
        self.silenceModeLabel.setObjectName("silenceModeLabel")
        self.horizontalLayout.addWidget(self.silenceModeLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.modeCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.modeCheckBox.setText("")
        self.modeCheckBox.setChecked(True)
        self.modeCheckBox.setObjectName("modeCheckBox")
        self.horizontalLayout.addWidget(self.modeCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mailLabel = QtWidgets.QLabel(self.centralWidget)
        self.mailLabel.setObjectName("mailLabel")
        self.horizontalLayout_2.addWidget(self.mailLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.mailLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.mailLineEdit.setObjectName("mailLineEdit")
        self.horizontalLayout_2.addWidget(self.mailLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sizeLabel = QtWidgets.QLabel(self.centralWidget)
        self.sizeLabel.setObjectName("sizeLabel")
        self.horizontalLayout_3.addWidget(self.sizeLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.sizeSpinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.sizeSpinBox.setObjectName("sizeSpinBox")
        self.sizeSpinBox.setMaximum(65536)
        self.horizontalLayout_3.addWidget(self.sizeSpinBox)
        self.bytesLabel = QtWidgets.QLabel(self.centralWidget)
        self.bytesLabel.setObjectName("bytesLabel")
        self.horizontalLayout_3.addWidget(self.bytesLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancelButton = QtWidgets.QPushButton(self.centralWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.okButton = QtWidgets.QPushButton(self.centralWidget)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_4.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.silenceModeLabel.setText(_translate("MainWindow", "Start silence mode"))
        self.mailLabel.setText(_translate("MainWindow", "E-Mail:"))
        self.mailLineEdit.setText(_translate("MainWindow", "Fyodorov.aleksej@gmail.com"))
        self.sizeLabel.setText(_translate("MainWindow", "Max size"))
        self.bytesLabel.setText(_translate("MainWindow", "Bytes"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.okButton.setText(_translate("MainWindow", "OK"))

