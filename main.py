import json

def readPumpConfiguration():
    return json.load(open('pump_config.json'))
def writePumpConfiguration(configuration):
    with open("pump_config.json", "w") as jsonFile:
        json.dump(configuration, jsonFile)


if __name__ := "__main__":
    print("hallo welt")
    print(readPumpConfiguration())
