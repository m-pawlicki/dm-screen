import npyscreen

class TopMenu(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleFixedText, name = "DM-Screen: Main Menu")
        self.add(npyscreen.TitleFixedText, name = "------------")
        self.choice = self.add(npyscreen.TitleSelectOne,
                               name="Select an Option:",
                               values=["Create Character", "Load Character", "List Characters", "Exit"],
                               scroll_exit=True)
        

    def on_ok(self):
        selection = self.choice.value
        if not selection:
            return
        match selection[0]:
            case 0:
                self.make_char()
            case 1:
                self.load_char()
            case 2:
                self.list_char()
            case 3:
                self.exit_app()
        self.editing = False

    def on_cancel(self):
        self.parentApp.setNextForm(None)
        self.editing = False

    def make_char(self):
        self.parentApp.setNextForm("CREATE")

    def load_char(self):
        self.parentApp.setNextForm("LOAD")

    def list_char(self):
        self.parentApp.setNextForm("LIST")

    def exit_app(self):
        self.parentApp.setNextForm(None)
        self.editing = False