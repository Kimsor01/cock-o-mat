import pprint
import sys

from Cockmixer import cockmixer
from qtpy import QtWidgets
from ui.mainwindow import Ui_cockomat
from buildUI import setupControls

cmix = cockmixer()
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window.setWindowTitle("Cock-o-mat")
ui_window = Ui_cockomat()
ui_window.setupUi(window)
setupControls(ui_window, cmix)

window.show()

sys.exit(app.exec())
