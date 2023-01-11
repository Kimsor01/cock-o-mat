import json
from booze import mixes


class cockmixer:
    def __init__(self):
        # self.running = False  # what is dis for?

        #  setup screen, pins, leds etc.
        self.valve_configuration = self.readValveConfig()
        self.drinkStats = self.readStats()
        self.availDrinks = []
        self.filterMixes()
        # pin.setup(self.valve_configuration[valve]["pin"],pin.out, initial = pin.high)

    def shutdown(self):
        self.writeValveConfig()
        self.writeStats()

    @staticmethod
    def readValveConfig():
        return json.load(open('JSON/valve_config.json'))

    @staticmethod
    def readStats():
        return json.load(open('JSON/drinkstats.json'))

    def writeValveConfig(self):
        with open("JSON/valve_config.json", "w") as jsonFile:
            json.dump(self.valve_configuration, jsonFile)

    def writeStats(self):
        with open("JSON/drinkstats.json", "w") as jsonFile:
            json.dump(self.drinkStats, jsonFile)

    def filterMixes(self):
        for i in mixes:
            ingred = {"ingredients": i["ingredients"]}["ingredients"]
            presentIng = 0
            for ing in ingred.keys():
                for v in self.valve_configuration.keys():
                    if ing == self.valve_configuration[v]["value"]:
                        presentIng += 1
            if presentIng == len(ingred.keys()):
                self.availDrinks.append(i)
        self.sortDrinksByStat()

    def GoToWork(self, drink, aua):
        for i in self.availDrinks:
            if i["name"] == drink:
                ingredients = {"ingredients": i["ingredients"]}["ingredients"]
                for ing in ingredients.keys():
                    for v in self.valve_configuration.keys():
                        if ing == self.valve_configuration[v]["value"]:
                            # valnum =int(''.join(filter(str.isdigit, v)))
                            amount = ingredients[ing]
                            if aua and int(v.isdigit()) < 7:
                                amount = amount * 2
                            print(v)
                            print("Pin " + str(self.valve_configuration[v]["pin"]) + " - " + str(amount) + "ml - " + ing)
        self.setStats(drink, aua)

    def setStats(self, drink, aua):
        for i in self.drinkStats.keys():
            if i == drink:
                self.drinkStats[i]["quantity"] += 1
                if aua:
                    self.drinkStats[i]["doubled"] += 1
                print(self.drinkStats[i])

    def sortDrinksByStat(self):
        p = {}
        for d in self.drinkStats.keys():
            for i in self.availDrinks:
                if d == i["name"]:
                    p[d] = self.drinkStats[d]["quantity"]
        return sorted(p.items(), key=lambda x: x[1], reverse=True)

