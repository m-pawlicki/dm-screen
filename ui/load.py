import npyscreen

class LoadMenu(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleText, name = "Character Name: ", value = "")

    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")