from booze import bottles

class controller:
    def __init__(self, window, cmix):
        self.window = window
        self.cmix = cmix

    def setupControls(self):
        for i in self.cmix.availDrinks:
            self.window.listWidget.addItem(i["name"])
            if self.window.comboBox.findText(i["type"]) != -1:
                continue
            self.window.comboBox.addItem(i["type"])
        self.window.comboBox.model().sort(0)

    def filterList(self):
        self.window.listWidget.clear()
        self.window.listWidget_2.clear()
        if self.window.comboBox.currentText() == "-":
            for i in self.cmix.availDrinks:
                self.window.listWidget.addItem(i["name"])
        else:
            for i in self.cmix.availDrinks:
                if i["type"] == self.window.comboBox.currentText():
                    self.window.listWidget.addItem(i["name"])

    def showAll(self):
        self.window.listWidget.clear()
        self.window.listWidget_2.clear()
        idx = self.window.comboBox.findText("-")
        if idx != -1:
            self.window.comboBox.setCurrentIndex(idx)
        for i in self.cmix.availDrinks:
            self.window.listWidget.addItem(i["name"])

    def showDetails(self):
        clicked = self.window.listWidget.currentItem()
        name = clicked.text()
        for i in self.cmix.availDrinks:
            if name == i["name"]:
                self.window.listWidget_2.addItem(i["name"] + " - " + i["type"])
                ingredients = {"ingredients": i["ingredients"]}["ingredients"]
                for ing in ingredients.keys():
                    for b in bottles:
                        if b["value"]==ing:
                            line = b["name"] + ": " + str(ingredients[ing]) + "ml"
                            self.window.listWidget_2.addItem(line)


