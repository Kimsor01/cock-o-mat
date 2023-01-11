import sys
from ui.mainwindow import Ui_cockomat
from Cockmixer import cockmixer
from qtpy import QtWidgets
from buildUI import controller


def main():
    cmix = cockmixer()
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("Cock-o-mat")
    ui_window = Ui_cockomat()
    ui_window.setupUi(window)
    kontrollörres = controller(ui_window, cmix)
    kontrollörres.setupControls()
    ui_window.cmbTypes.currentTextChanged.connect(kontrollörres.filterList)
    ui_window.pbShowAll.clicked.connect(kontrollörres.showAll)
    ui_window.listDrinkSelection.clicked.connect(kontrollörres.showDetails)
    ui_window.pbPourDrink.clicked.connect(kontrollörres.pour)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
