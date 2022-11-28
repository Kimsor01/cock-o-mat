def setupControls(Ui_cockomat, cockmixer):
    for i in cockmixer.availDrinks:
        Ui_cockomat.listWidget.addItem(i["name"])
        if Ui_cockomat.comboBox.findText(i["type"]) != -1:
            continue
        Ui_cockomat.comboBox.addItem(i["type"])
    Ui_cockomat.comboBox.model().sort(0)

