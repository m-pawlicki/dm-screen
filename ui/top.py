import npyscreen

class TopMenu(npyscreen.Form):
    def create(self):
        F  = npyscreen.Form(name = "DM-Screen - Main Menu")
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Choose an option:",
                values = ["Create Character","Load Character"], scroll_exit=True)
        

        
        F.edit()
    
    def afterEditing(self):
        self.parentApp.setNextForm(None)