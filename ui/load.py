import npyscreen

class LoadMenu(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleFixedText, name = "DM-Screen: Load a Character")
        self.add(npyscreen.TitleFixedText, name = "------------")
        self.search_term = self.add(npyscreen.TitleText, name = "Search for which character?", value = "")

    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")