import sys
from MainWindow import MainWindow
from qtpy import QtWidgets
from Controller import controller


def main2():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    kontrollörres = controller(window.ui, window.cmix)
    kontrollörres.setupControls()
    window.ui.cmbTypes.currentTextChanged.connect(kontrollörres.filterList)
    window.ui.pbShowAll.clicked.connect(kontrollörres.showAll)
    window.ui.listDrinkSelection.clicked.connect(kontrollörres.showDetails)
    window.ui.pbPourDrink.clicked.connect(kontrollörres.pour)
    sys.exit(app.exec())


if __name__ == "__main__":
    main2()
