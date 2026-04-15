import npyscreen
from utils import db

class LoadMenu(npyscreen.ActionForm):
    def create(self):
        self.name = "DM-Screen: Load Character"
        self.search = self.add(npyscreen.TitleText, name = "Search for which character?")

    def on_ok(self):
        try:
            self.res = self.parentApp.database.get_character_by_name(str(self.search.value))
            self.parentApp.getForm("CREATE").value = self.res[0]
            self.parentApp.switchForm("CREATE")
        except:
            msg = "Character not found.\n\nHit TAB and then ENTER to confirm."
            npyscreen.notify_confirm(msg, title="Error")

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

    def afterEditing(self):
        self.parentApp.switchFormPrevious()