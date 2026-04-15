import npyscreen
from utils import db

class ListCharacter(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(ListCharacter, self).__init__(*args, **keywords)
        self.add_handlers({
            "^A": self.when_add_character,
            "^D": self.when_delete_character,
            "^X": self.when_cancel
        })

    def display_value(self, vl):
        return f"Character: {vl[1]} | Player: {vl[2]}"

    def actionHighlighted(self, act_on_this, key_press):
        self.parent.parentApp.getForm("CREATE").value = act_on_this[0]
        self.parent.parentApp.switchForm("CREATE")

    def when_add_character(self, *args, **keywords):
        self.parent.parentApp.getForm("CREATE").value = None
        self.parent.parentApp.switchForm("CREATE")

    def when_delete_character(self, *args, **keywords):
        count = self.parent.parentApp.database.list_characters()
        if len(count) != 0:
            self.parent.parentApp.database.delete_character_by_id(self.values[self.cursor_line][0])
        self.parent.update_list()

    def when_cancel(self, *args, **keywords):
        self.parent.parentApp.switchFormPrevious()

class ListMenu(npyscreen.FormMutt):

    MAIN_WIDGET_CLASS = ListCharacter

    def beforeEditing(self):
        self.update_list()

    def update_list(self):
        self.wMain.values = self.parentApp.database.list_characters()
        self.wMain.display()