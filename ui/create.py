import npyscreen
from models import alignment
from models import classes
from models import races

job_list = [c.value for c in classes.ClassType]
race_list = [r.value for r in races.RaceType]
align_list = [a.value for a in alignment.AlignmentType]

class CreateMenu(npyscreen.FormMultiPageAction):

    def create(self):
        self.value = None
        self.char_name = self.add(npyscreen.TitleText, name = "Character:")
        self.player_name = self.add(npyscreen.TitleText, name = "Player:")
        self.char_class = self.add(npyscreen.TitleSelectOne, name = "Class:", values = job_list, max_height = 3, value = [1,], scroll_exit = True)
        self.char_level = self.add(npyscreen.TitleSlider, name = "Level:", lowest = 1, step = 1, out_of = 20)
        self.char_bg = self.add(npyscreen.TitleText, name = "Background:")
        self.char_race = self.add(npyscreen.TitleSelectOne, name = "Race:", values = race_list, max_height = 3, value = [1,], scroll_exit = True)
        self.char_align = self.add(npyscreen.TitleSelectOne, name = "Alignment:", values = align_list, max_height = 3, value = [1,], scroll_exit = True)
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
            self.char_class.value = job_list.index(character[3])
            self.char_level.value = character[4]
            self.char_bg.value = character[5]
            self.char_race.value = race_list.index(character[6])
            self.char_align.value = align_list.index(character[7])
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
            self.char_level.value = 1
            self.char_bg.value = ''
            self.char_race.value = ''
            self.char_align.value = ''
            self.char_exp.value = '0'
            self.char_str.value = '10'
            self.char_dex.value = '10'
            self.char_con.value = '10'
            self.char_int.value = '10'
            self.char_wis.value = '10'
            self.char_cha.value = '10'

    def on_ok(self):
        try:
            if self.char_id:
                self.parentApp.database.update_character(
                    char_id=self.char_id, 
                    char_name=self.char_name.value, 
                    player_name=self.player_name.value, 
                    job=self.char_class.values[self.char_class.value[0]], 
                    level=int(self.char_level.value), 
                    bg=self.char_bg.value, 
                    race=self.char_race.values[self.char_race.value[0]], 
                    alignment=self.char_align.values[self.char_align.value[0]], 
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
                    job=self.char_class.values[self.char_class.value[0]], 
                    level=int(self.char_level.value), 
                    bg=self.char_bg.value, 
                    race=self.char_race.values[self.char_race.value[0]], 
                    alignment=self.char_align.values[self.char_align.value[0]], 
                    exp=int(self.char_exp.value), 
                    str=int(self.char_str.value),
                    dex=int(self.char_dex.value),
                    con=int(self.char_con.value),
                    int=int(self.char_int.value),
                    wis=int(self.char_wis.value),
                    cha=int(self.char_cha.value)
                )

            self.parentApp.switchFormPrevious()

        except Exception as e:
            msg = f"Error: {e}"
            npyscreen.notify_wait(msg, title="Error")


    def on_cancel(self):
        self.parentApp.switchFormPrevious()