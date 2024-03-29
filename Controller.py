import os
import time
from random import randrange
import threading
from booze import bottles
from playsound import playsound


class Controller:
    def __init__(self, qWidget, cmix):
        self.qWidget = qWidget  # the actual MainWindow
        self.window = qWidget.ui  # despite the name only the UI components, to lazy to refactor
        self.cmix = cmix
        self.cwd = os.getcwd()

    def setupControls(self):
        for i in self.cmix.availDrinks:
            self.window.listDrinkSelection.addItem(i["name"])
            if self.window.cmbTypes.findText(i["type"]) != -1:
                continue
            self.window.cmbTypes.addItem(i["type"])
        self.window.listDrinkSelection.setCurrentRow(0)
        self.window.cmbTypes.addItem("Top 5 😍")
        self.window.cmbTypes.addItem("Low 5 🤮")
        self.window.cmbTypes.model().sort(0)
        # threading.Thread(target=playsound, args=(self.cwd + "/memes/sounds/okletsgo.mp3", "block=False"),
        #                  daemon=True).start()

    def filterList(self):
        self.window.listDrinkSelection.clear()
        self.window.listDrinkDetails.clear()
        self.window.labelDrink.clear()
        self.window.listDrinkSelection.setSortingEnabled(True)
        if self.window.cmbTypes.currentText() == "-":
            for i in self.cmix.availDrinks:
                self.window.listDrinkSelection.addItem(i["name"])
        elif self.window.cmbTypes.currentText() == "Top 5 😍":
            if randrange(5) == 1:
                threading.Thread(target=playsound, args=(self.cwd + "/memes/sounds/yeay.mp3", "block=False"),
                                 daemon=True).start()
            sortedlist = self.cmix.sortDrinksByStat()
            for g in range(0, 5):
                self.window.listDrinkSelection.setSortingEnabled(False)
                self.window.listDrinkSelection.addItem(sortedlist[g][0])
        elif self.window.cmbTypes.currentText() == "Low 5 🤮":
            if randrange(5) == 1:
                threading.Thread(target=playsound, args=(self.cwd + "/memes/sounds/puke.mp3", "block=False"),
                                 daemon=True).start()
            sortedlist = self.cmix.sortDrinksByStat()
            for g in range(-6, -1):
                self.window.listDrinkSelection.setSortingEnabled(False)
                self.window.listDrinkSelection.addItem(sortedlist[g][0])
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
        lines = []
        clicked = self.window.listDrinkSelection.currentItem()
        if clicked is None:
            return
        name = clicked.text()
        for i in self.cmix.availDrinks:
            if name == i["name"]:
                self.window.labelDrink.setText(i["name"])
                ingredients = {"ingredients": i["ingredients"]}["ingredients"]
                for ing in ingredients.keys():
                    for b in bottles:
                        if b["value"] == ing:
                            line = b["name"] + ": " + str(ingredients[ing]) + "ml"
                            lines.append(line)
                            # self.window.listDrinkDetails.addItem(line)
        for line in sorted(lines):
            self.window.listDrinkDetails.addItem(line)
        self.window.listDrinkDetails.addItem("")
        for d in self.cmix.drinkStats.keys():
            if d == name:
                line = "Bestellungen: " + str(self.cmix.drinkStats[d]["quantity"])
                self.window.listDrinkDetails.addItem(line)
                line = "davon mit extra Umdrehungen: " + str(self.cmix.drinkStats[d]["doubled"])
                self.window.listDrinkDetails.addItem(line)

    def updateDetails(self, drink):
        rows = self.window.listDrinkDetails.count()
        self.window.listDrinkDetails.takeItem(rows - 1)
        self.window.listDrinkDetails.takeItem(rows - 2)
        for d in self.cmix.drinkStats.keys():
            if d == drink:
                line = "Bestellungen: " + str(self.cmix.drinkStats[d]["quantity"])
                self.window.listDrinkDetails.addItem(line)
                line = "davon mit extra Umdrehungen: " + str(self.cmix.drinkStats[d]["doubled"])
                self.window.listDrinkDetails.addItem(line)

    def pour(self):
        drink = self.window.labelDrink.text()
        aua = self.window.cbAua.isChecked()
        self.enableLoadingBar(True)
        self.cmix.GoToWork(drink, aua)
        self.enableLoadingBar(False)
        self.updateDetails(drink)

    def enableLoadingBar(self, mode: bool):
        # toggled hide() bei allen controlls entsprechend dem übergebenen boolean wert
        # die loadingbar wird entgegen gesetzt getoggled
        self.window.listDrinkSelection.setHidden(mode)
        self.window.listDrinkDetails.setHidden(mode)
        self.window.pbOptions.setHidden(mode)
        self.window.pbPourDrink.setHidden(mode)
        self.window.cmbTypes.setHidden(mode)
        self.window.pbFart.setHidden(mode)
        self.window.pbRandom.setHidden(mode)
        self.window.pbShowAll.setHidden(mode)
        self.window.labelDrink.setHidden(mode)
        self.window.cbAua.setHidden(mode)
        self.window.ldBar.setHidden(not mode)
        self.window.ldBar.reset()
        self.qWidget.repaint()  # repaint not recommended but necessary as update is put in q until back in main thread

    def progressBar(self, amount: int):
        cur = self.window.ldBar.value()
        total = cur + amount
        while cur < total:
            if cur + 5 >= total:
                self.window.ldBar.setValue(total)
                return
            self.window.ldBar.setValue(cur + 5)  # TODO: replace 5 with actual output per sec
            time.sleep(0.5)
            cur = self.window.ldBar.value()

    def fart(self):
        if randrange(100) == 1:
            threading.Thread(target=playsound, args=(self.cwd + "/memes/sounds/diarrhea.mp3", "block=False"),
                             daemon=True).start()
        else:
            threading.Thread(target=playsound, args=(self.cwd + "/memes/sounds/fart{}.mp3".format(randrange(3)),
                                                     "block=False"), daemon=True).start()

    def selectRandom(self):
        x = randrange(len(self.cmix.availDrinks))
        self.window.listDrinkSelection.setCurrentRow(x)

    def doubleUp(self):
        if self.window.cbAua.isChecked() is False:
            self.showDetails()
        else:
            self.window.listDrinkDetails.clear()
            lines = []
            clicked = self.window.listDrinkSelection.currentItem()
            if clicked is None:
                return
            name = clicked.text()
            for i in self.cmix.availDrinks:
                if name == i["name"]:
                    self.window.labelDrink.setText(i["name"])
                    ingredients = {"ingredients": i["ingredients"]}["ingredients"]
                    for ing in ingredients.keys():
                        count = 0
                        for b in bottles:
                            if b["value"] == ing:
                                amount = ingredients[ing]
                                if count < 6:
                                    amount = amount * 2
                                line = b["name"] + ": " + str(amount) + "ml"
                                lines.append(line)
                                # self.window.listDrinkDetails.addItem(line)
                            count += 1
            for line in sorted(lines):
                self.window.listDrinkDetails.addItem(line)
            self.window.listDrinkDetails.addItem("")
            for d in self.cmix.drinkStats.keys():
                if d == name:
                    line = "Bestellungen: " + str(self.cmix.drinkStats[d]["quantity"])
                    self.window.listDrinkDetails.addItem(line)
                    line = "davon mit extra Umdrehungen: " + str(self.cmix.drinkStats[d]["doubled"])
                    self.window.listDrinkDetails.addItem(line)

    def getRecipes(self):
        try:
            os.remove("C:/void/CocktailRezepte.txt")
        except OSError:
            pass
        with open("C:/void/CocktailRezepte.txt", "a") as file:
            clicked = self.window.listDrinkSelection.currentItem()
            if clicked is None:
                if self.window.cmbTypes.currentText() == "-":
                    for i in self.cmix.availDrinks:
                        if i["type"] == self.window.cmbTypes.currentText():
                            file.write(i["name"] + "\n")
                            ingredients = {"ingredients": i["ingredients"]}["ingredients"]
                            for ing in ingredients.keys():
                                for b in bottles:
                                    if b["value"] == ing:
                                        file.write("\t" + b["name"] + ": " + str(ingredients[ing]) + "ml" + "\n")
                            file.write("\n")
                else:
                    for i in self.cmix.availDrinks:
                        if i["type"] == self.window.cmbTypes.currentText():
                            file.write(i["name"] + "\n")
                            ingredients = {"ingredients": i["ingredients"]}["ingredients"]
                            for ing in ingredients.keys():
                                for b in bottles:
                                    if b["value"] == ing:
                                        file.write("\t" + b["name"] + ": " + str(ingredients[ing]) + "ml" + "\n")
                            file.write("\n")
            else:
                name = clicked.text()
                for i in self.cmix.availDrinks:
                    if name == i["name"]:
                        file.write(name + "\n")
                        ingredients = {"ingredients": i["ingredients"]}["ingredients"]
                        for ing in ingredients.keys():
                            for b in bottles:
                                if b["value"] == ing:
                                    file.write("\t" + b["name"] + ": " + str(ingredients[ing]) + "ml" + "\n")
                        file.write("\n")
        file.close()
