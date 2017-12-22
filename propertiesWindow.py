import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, qApp, QMenu
import properties
from mainwindow import Ui_MainWindow

class MyWin(QtWidgets.QMainWindow):
    tray_icon = None
    curProp = None
    acceptSignal = pyqtSignal(properties.Properties)

    # construct window
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curProp = properties.load()

        self.ui.sizeSpinBox.setValue(self.curProp.size)
        self.ui.mailLineEdit.setText(self.curProp.address)
        self.ui.modeCheckBox.setChecked(self.curProp.silenceMode)

        self.ui.okButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.canceled)

        #self.tray_icon = QSystemTrayIcon(self)
        #self.tray_icon.setIcon(QIcon(os.getcwd() + "/tray.png"))#QQQQQ
        #show_action = QAction("Show", self)
        #quit_action = QAction("Exit", self)
        #hide_action = QAction("Hide", self)
        #show_action.triggered.connect(self.show)
        #hide_action.triggered.connect(self.hide)
        #quit_action.triggered.connect(qApp.quit)
        #tray_menu = QMenu()
        #tray_menu.addAction(show_action)
        #tray_menu.addAction(hide_action)
        #tray_menu.addAction(quit_action)
        #self.tray_icon.setContextMenu(tray_menu)
        #self.tray_icon.show()
        #self.hide()QQQ

    def accept(self):
        cur = properties.Properties(self.ui.modeCheckBox.isChecked(), self.ui.mailLineEdit.text(), self.ui.sizeSpinBox.value())
        self.acceptSignal.emit(cur)
        self.curProp = cur
        self.refresh()
        self.hide()

    def canceled(self):
        self.hide()

    def refresh(self):
        self.ui.sizeSpinBox.setValue(self.curProp.size)
        self.ui.mailLineEdit.setText(self.curProp.address)
        self.ui.modeCheckBox.setChecked(self.curProp.silenceMode)

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.hide()#QQQQ