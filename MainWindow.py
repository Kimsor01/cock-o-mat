from PyQt5.QtWidgets import QWidget, QMessageBox
from Cockmixer import cockmixer
from ui.cock_ui import Ui_cockomat


class MainWindow(QWidget):
    cmix: cockmixer

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_cockomat()
        self.ui.setupUi(self)
        self.cmix = cockmixer()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Exit", "Cock-o-mat beenden?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.cmix.shutdown()
            event.accept()
        else:
            event.ignore()
