import pprint
import sys
from ui.mainwindow import Ui_cockomat
from Cockmixer import cockmixer
from qtpy import QtWidgets
from buildUI import controller

cmix = cockmixer()
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window.setWindowTitle("Cock-o-mat")
ui_window = Ui_cockomat()
ui_window.setupUi(window)
kontrollörres = controller(ui_window, cmix)
kontrollörres.setupControls()
ui_window.comboBox.currentTextChanged.connect(kontrollörres.filterList)
ui_window.pushButton.pressed.connect(kontrollörres.showAll)
ui_window.listWidget.clicked.connect(kontrollörres.showDetails)

window.show()

sys.exit(app.exec())
