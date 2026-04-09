import npyscreen
from utils import db

class LoadMenu(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleFixedText, name = "DM-Screen: Load a Character")
        self.add(npyscreen.TitleFixedText, name = "------------")
        self.search_term = self.add(npyscreen.TitleText, name = "Search for which character?")

    def on_ok(self):
        self.parentApp.database.get_character_by_name(self.search_term)

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")