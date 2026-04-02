import npyscreen

class CreateMenu(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleFixedText, name = "DM-Screen: Create a Character")
        self.add(npyscreen.TitleFixedText, name = "------------")
        self.add(npyscreen.TitleText, name = "Character Name:", value = "")
        self.add(npyscreen.TitleText, name = "Player Name:", value = "")
        self.add(npyscreen.TitleText, name = "Class:", value = "")
        self.add(npyscreen.TitleSlider, name = "Level:", lowest = 1, out_of = 20)
        self.add(npyscreen.TitleText, name = "Race:", value = "")
        self.add(npyscreen.TitleText, name = "Alignment:", value = "")
    
    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")