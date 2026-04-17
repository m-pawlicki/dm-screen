import npyscreen

class CreateMenu(npyscreen.ActionForm):
    def create(self):
        self.value = None
        self.char_name = self.add(npyscreen.TitleText, name = "Character:")
        self.player_name = self.add(npyscreen.TitleText, name = "Player:")
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
            self.name = f"DM-Screen: Editing character {character[1]}"
            self.char_id = character[0]
            self.char_name.value = character[1]
            self.player_name.value = character[2]
            self.char_class.value = character[3]
            self.char_level.value = str(character[4])
            self.char_bg.value = character[5]
            self.char_race.value = character[6]
            self.char_align.value = character[7]
            self.char_exp.value = str(character[8])
            self.char_str.value = str(character[9])
            self.char_dex.value = str(character[10])
            self.char_con.value = str(character[11])
            self.char_int.value = str(character[12])
            self.char_wis.value = str(character[13])
            self.char_cha.value = str(character[14])
        else:
            self.name = "DM-Screen: New Character"
            self.char_id = ''
            self.char_name.value = ''
            self.player_name.value = ''
            self.char_class.value = ''
            self.char_level.value = ''
            self.char_bg.value = ''
            self.char_race.value = ''
            self.char_align.value = ''
            self.char_exp.value = ''
            self.char_str.value = ''
            self.char_dex.value = ''
            self.char_con.value = ''
            self.char_int.value = ''
            self.char_wis.value = ''
            self.char_cha.value = ''

    def on_ok(self):
        try:
            if self.char_id:
                self.parentApp.database.update_character(
                    char_id=self.char_id, 
                    char_name=self.char_name.value, 
                    player_name=self.player_name.value, 
                    job=self.char_class.value, 
                    level=int(self.char_level.value), 
                    bg=self.char_bg.value, 
                    race=self.char_race.value, 
                    alignment=self.char_align.value, 
                    exp=int(self.char_exp.value), 
                    str=int(self.char_str.value),
                    dex=int(self.char_dex.value),
                    con=int(self.char_con.value),
                    int=int(self.char_int.value),
                    wis=int(self.char_wis.value),
                    cha=int(self.char_cha.value))
            else:
                self.parentApp.database.add_character(
                    char_name=self.char_name.value, 
                    player_name=self.player_name.value, 
                    job=self.char_class.value, 
                    level=int(self.char_level.value), 
                    bg=self.char_bg.value, 
                    race=self.char_race.value, 
                    alignment=self.char_align.value, 
                    exp=int(self.char_exp.value), 
                    str=int(self.char_str.value),
                    dex=int(self.char_dex.value),
                    con=int(self.char_con.value),
                    int=int(self.char_int.value),
                    wis=int(self.char_wis.value),
                    cha=int(self.char_cha.value)
                )
            self.parentApp.switchFormPrevious()

        except:
            msg = "Data mismatch. Please use integers for level, experience, and stats.\n\nHit TAB and then ENTER to confirm."
            npyscreen.notify_confirm(msg, title="Error")


    def on_cancel(self):
        self.parentApp.switchFormPrevious()
    
    def afterEditing(self):
        self.parentApp.switchFormPrevious()