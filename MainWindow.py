from PyQt5 import QtWidgets, QtCore
from Cockmixer import cockmixer
from Controller import Controller
from ui.cock_ui import Ui_cockomat


class MainWindow(QtWidgets.QWidget):
    cmix: cockmixer
    kontrollörres: Controller

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_cockomat()
        self.ui.setupUi(self)
        self.setWindowFlags(
            self.windowFlags() |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint
        )
        self.cmix = cockmixer()
        self.kontrollörres = Controller(self, self.cmix)
        self.cmix.kontrollörres = self.kontrollörres

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Exit", "Cock-o-mat beenden?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.cmix.shutdown()
            event.accept()
        else:
            event.ignore()
