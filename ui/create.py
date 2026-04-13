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
        if self.value:
            character = self.parentApp.database.get_character_by_id(self.value)
            self.name = "Editing character: %s" % character[1]
            self.char_id = character[0]
            self.char_name = character[1]
            self.player_name = character[2]
            self.char_class = character[3]
            self.char_level = character[4]
            self.char_bg = character[5]
            self.char_race = character[6]
            self.char_align = character[7]
            self.char_exp = character[8]
            self.char_str = character[9]
            self.char_dex = character[10]
            self.char_con = character[11]
            self.char_int = character[12]
            self.char_wis = character[13]
            self.char_cha = character[14]
        else:
            self.name = "New Character"
            self.char_id = ''
            self.char_name = ''
            self.player_name = ''
            self.char_class = ''
            self.char_level = ''
            self.char_bg = ''
            self.char_race = ''
            self.char_align = ''
            self.char_exp = ''
            self.char_str = ''
            self.char_dex = ''
            self.char_con = ''
            self.char_int = ''
            self.char_wis = ''
            self.char_cha = ''

    def on_ok(self):
        if self.char_id:
            self.parentApp.database.update_character(
                self.char_id, 
                self.char_name, 
                self.player_name, 
                self.char_class, 
                self.char_level, 
                self.char_bg, 
                self.char_race, 
                self.char_align, 
                self.char_exp, 
                self.char_str,
                self.char_dex,
                self.char_con,
                self.char_int,
                self.char_wis,
                self.char_cha)
        else:
            self.parentApp.database.add_character(
                self.char_name, 
                self.player_name, 
                self.char_class, 
                self.char_level, 
                self.char_bg, 
                self.char_race, 
                self.char_align, 
                self.char_exp, 
                self.char_str,
                self.char_dex,
                self.char_con,
                self.char_int,
                self.char_wis,
                self.char_cha
            )

        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()
    
    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")