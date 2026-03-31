import npyscreen

class CreateMenu(npyscreen.Form):
    def create(self):
        F  = npyscreen.Form(name = "DM-Screen - Create Character")
        F.edit()

    
    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")