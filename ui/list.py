import npyscreen
from utils import db

class ListCharacter(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(ListCharacter, self).__init__(*args, **keywords)
        self.add_handlers({
            "^A": self.when_add_record,
            "^D": self.when_delete_record
        })

    def display_value(self, vl):
        return "Character: %s, Player: %s" % (vl[1], vl[2])

    def actionHighlighted(self, act_on_this, key_press):
        self.parent.parentApp.getForm('CREATE').value =act_on_this[0]
        self.parent.parentApp.switchForm('CREATE')

    def when_add_record(self, *args, **keywords):
        self.parent.parentApp.getForm('CREATE').value = None
        self.parent.parentApp.switchForm('CREATE')

    def when_delete_record(self, *args, **keywords):
        self.parent.parentApp.database.delete_character(self.values[self.cursor_line][0])
        self.parent.update_list()

class ListMenu(npyscreen.FormMutt):

    MAIN_WIDGET_CLASS = ListCharacter

    def beforeEditing(self):
        self.update_list()

    def update_list(self):
        self.wMain.values = self.parentApp.database.list_characters()
        self.wMain.display()