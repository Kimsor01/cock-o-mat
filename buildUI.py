from booze import bottles


class controller:
    def __init__(self, window, cmix):
        self.window = window
        self.cmix = cmix

    def setupControls(self):
        for i in self.cmix.availDrinks:
            self.window.listDrinkSelection.addItem(i["name"])
            if self.window.cmbTypes.findText(i["type"]) != -1:
                continue
            self.window.cmbTypes.addItem(i["type"])
        self.window.cmbTypes.model().sort(0)

    def filterList(self):
        self.window.listDrinkSelection.clear()
        self.window.listDrinkDetails.clear()
        self.window.labelDrink.clear()
        if self.window.cmbTypes.currentText() == "-":
            for i in self.cmix.availDrinks:
                self.window.listDrinkSelection.addItem(i["name"])
        else:
            for i in self.cmix.availDrinks:
                if i["type"] == self.window.cmbTypes.currentText():
                    self.window.listDrinkSelection.addItem(i["name"])

    def showAll(self):
        if self.window.cmbTypes.currentText() == '-':
            pass
        else:
            self.window.listDrinkSelection.clear()
            self.window.listDrinkDetails.clear()
            self.window.labelDrink.clear()
            idx = self.window.cmbTypes.findText("-")
            if idx != -1:
                self.window.cmbTypes.setCurrentIndex(idx)

    def showDetails(self):
        self.window.listDrinkDetails.clear()
        self.window.cbAua.setChecked(False)
        clicked = self.window.listDrinkSelection.currentItem()
        name = clicked.text()
        for i in self.cmix.availDrinks:
            if name == i["name"]:
                self.window.labelDrink.setText(i["name"])
                ingredients = {"ingredients": i["ingredients"]}["ingredients"]
                for ing in ingredients.keys():
                    for b in bottles:
                        if b["value"] == ing:
                            line = b["name"] + ": " + str(ingredients[ing]) + "ml"
                            self.window.listDrinkDetails.addItem(line)

    def pour(self):
        drink = self.window.labelDrink.text()
        aua = self.window.cbAua.isChecked()
        self.cmix.GoToWork(drink, aua)
