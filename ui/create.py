import npyscreen

class CreateMenu(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleFixedText, name = "DM-Screen: Create a Character")
        self.add(npyscreen.TitleFixedText, name = "------------")
        self.char_name = self.add(npyscreen.TitleText, name = "Character Name:", value = "")
        self.player_name = self.add(npyscreen.TitleText, name = "Player Name:", value = "")
        self.char_class = self.add(npyscreen.TitleText, name = "Class:", value = "")
        self.char_level = self.add(npyscreen.TitleText, name = "Level:", value = "1")
        self.char_bg = self.add(npyscreen.TitleText, name = "Background: ")
        self.char_race = self.add(npyscreen.TitleText, name = "Race:", value = "")
        self.char_align = self.add(npyscreen.TitleText, name = "Alignment:", value = "")
        self.char_exp = self.add(npyscreen.TitleText, name = "Experience:", value = "0")
        self.char_str = self.add(npyscreen.TitleText, name = "Strength:", value = "0")
        self.char_dex = self.add(npyscreen.TitleText, name = "Dexterity:", value = "0")
        self.char_con = self.add(npyscreen.TitleText, name = "Constitution:", value = "0")
        self.char_int = self.add(npyscreen.TitleText, name = "Intelligence:", value = "0")
        self.char_wis = self.add(npyscreen.TitleText, name = "Wisdom:", value = "0")
        self.char_cha = self.add(npyscreen.TitleText, name = "Charisma:", value = "0")
    
    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")