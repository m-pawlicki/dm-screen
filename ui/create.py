import npyscreen

class CreateMenu(npyscreen.ActionForm):
    def create(self):
        self.value = None
        self.add(npyscreen.TitleFixedText, name = "DM-Screen: Character Sheet")
        self.add(npyscreen.TitleFixedText, name = "------------")
        self.char_name = self.add(npyscreen.TitleText, name = "Character Name:")
        self.player_name = self.add(npyscreen.TitleText, name = "Player Name:")
        self.char_class = self.add(npyscreen.TitleText, name = "Class:")
        self.char_level = self.add(npyscreen.TitleText, name = "Level:")
        self.char_bg = self.add(npyscreen.TitleText, name = "Background:")
        self.char_race = self.add(npyscreen.TitleText, name = "Race:")
        self.char_align = self.add(npyscreen.TitleText, name = "Alignment:")
        self.char_exp = self.add(npyscreen.TitleText, name = "Experience:")
        self.char_str = self.add(npyscreen.TitleText, name = "Strength:")
        self.char_dex = self.add(npyscreen.TitleText, name = "Dexterity:")
        self.char_con = self.add(npyscreen.TitleText, name = "Constitution:")
        self.char_int = self.add(npyscreen.TitleText, name = "Intelligence:")
        self.char_wis = self.add(npyscreen.TitleText, name = "Wisdom:")
        self.char_cha = self.add(npyscreen.TitleText, name = "Charisma:")

    def beforeEditing(self):
        pass

    def on_ok(self):
        pass

    def on_cancel(self):
        self.parentApp.switchFormPrevious()
    
    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")