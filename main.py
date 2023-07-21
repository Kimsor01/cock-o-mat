import sys
from MainWindow import MainWindow
from qtpy import QtWidgets
from Controller import Controller


# !!! BEI BUILD MIT AUTO-PY-TO-EXE MÜSSEN JSON-/MEME-FOLDER SOWIE QRAIBOWSTYLES HUNZUGEFÜGT WERDEN !!!
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    kontrollörres = Controller(window, window.cmix)
    kontrollörres.setupControls()
    window.ui.cmbTypes.currentTextChanged.connect(kontrollörres.filterList)
    window.ui.pbShowAll.clicked.connect(kontrollörres.showAll)
    window.ui.listDrinkSelection.clicked.connect(kontrollörres.showDetails)
    window.ui.listDrinkSelection.currentItemChanged.connect(kontrollörres.showDetails)
    window.ui.pbPourDrink.clicked.connect(kontrollörres.pour)
    window.ui.pbFart.clicked.connect(kontrollörres.fart)
    window.ui.pbRandom.clicked.connect(kontrollörres.selectRandom)
    window.ui.cbAua.toggled.connect(kontrollörres.doubleUp)
    window.ui.pbOptions.clicked.connect(kontrollörres.getRecipes)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
