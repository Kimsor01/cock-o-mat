import json
import pprint

from booze import bottles, mixes


class cockmixer:
    def __init__(self):
        self.running = False  # what is dis for?

        #  setup screen, pins, leds etc.
        self.valve_configuration = self.readValveConfig()
        self.availDrinks = []
        self.filterMixes()
        # pin.setup(self.valve_configuration[valve]["pin"],pin.out, initial = pin.high)

    @staticmethod
    def readValveConfig():
        return json.load(open('valve_config.json'))

    # def writeValveConfig(configuration):
    #     with open("valve_config.json", "w") as jsonFile:
    #         json.dump(configuration, jsonFile)

    def filterMixes(self):
        for i in mixes:
            attri = {"ingredients": i["ingredients"]}
            ingred = attri["ingredients"]
            presentIng = 0
            for ing in ingred.keys():
                for v in self.valve_configuration.keys():
                    if ing == self.valve_configuration[v]["value"]:
                        presentIng += 1
            if presentIng != len(ingred.keys()):
                i["mixable"] = "False"
            else:
                self.availDrinks.append(i)
