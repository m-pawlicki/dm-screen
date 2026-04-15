import npyscreen
from utils import db

class LoadMenu(npyscreen.ActionForm):
    def create(self):
        self.name = "DM-Screen: Load Character"
        self.search = self.add(npyscreen.TitleText, name = "Search for which character?")

    def on_ok(self):
        search = str(self.search)
        self.parentApp.database.get_character_by_name(search)

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")