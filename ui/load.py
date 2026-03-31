import npyscreen

class LoadMenu(npyscreen.Form):
    def create(self):
        F  = npyscreen.Form(name = "DM-Screen - Load Character")
        self.add(npyscreen.TitleText, name = "Character Name: ", value= "")
        
        F.edit()
    
    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")