import sys
from MainWindow import MainWindow
from qtpy import QtWidgets


# !!! BEI BUILD MIT AUTO-PY-TO-EXE MÜSSEN JSON-/MEME-FOLDER SOWIE QRAIBOWSTYLES HUNZUGEFÜGT WERDEN !!!
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.kontrollörres.setupControls()
    window.show()
    # kontrollörres = Controller(window, window.cmix)
    # kontrollörres.setupControls()
    window.ui.cmbTypes.currentTextChanged.connect(window.kontrollörres.filterList)
    window.ui.pbShowAll.clicked.connect(window.kontrollörres.showAll)
    window.ui.listDrinkSelection.clicked.connect(window.kontrollörres.showDetails)
    window.ui.listDrinkSelection.currentItemChanged.connect(window.kontrollörres.showDetails)
    window.ui.pbPourDrink.clicked.connect(window.kontrollörres.pour)
    window.ui.pbFart.clicked.connect(window.kontrollörres.fart)
    window.ui.pbRandom.clicked.connect(window.kontrollörres.selectRandom)
    window.ui.cbAua.toggled.connect(window.kontrollörres.doubleUp)
    # window.ui.pbOptions.clicked.connect(window.kontrollörres.getRecipes)
    window.ui.pbOptions.clicked.connect(window.close)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
