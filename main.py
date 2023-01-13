import os
import sys

from playsound import playsound

from MainWindow import MainWindow
from qtpy import QtWidgets
from Controller import Controller


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    kontrollörres = Controller(window.ui, window.cmix)
    kontrollörres.setupControls()
    window.ui.cmbTypes.currentTextChanged.connect(kontrollörres.filterList)
    window.ui.pbShowAll.clicked.connect(kontrollörres.showAll)
    window.ui.listDrinkSelection.clicked.connect(kontrollörres.showDetails)
    window.ui.listDrinkSelection.currentItemChanged.connect(kontrollörres.showDetails)
    window.ui.pbPourDrink.clicked.connect(kontrollörres.pour)
    window.ui.pbFart.clicked.connect(kontrollörres.fart)
    window.ui.pbRandom.clicked.connect(kontrollörres.selectRandom)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
