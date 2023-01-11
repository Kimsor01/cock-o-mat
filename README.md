# sth cool about cock-o-mat V0.1

# def buildMenu(self, bottles, mixes):

        # add possible mixes
        mix_opts = []
        for mix in mixes:
            mix_opts.append(MenuItem(mix["type"], mix["name"],{"ingeredients": mix["ingredients"]}))

        # pump config
        configuration_menu = Menu("Config")

        valve_opts =[]
        for v in sorted(self.valve_configuration.keys()):
            config = Menu(self.valve_configuration[v]["name"])
            # add drink opt for each valve
            for b in bottles:
                selected = "*" if b["value"] == self.valve_configuration[v]["value"] else ""
                config.addOption(MenuItem('valve_selection', b["name"], {"key":v, "value": b["value"], "name": b["name"]}))
      
