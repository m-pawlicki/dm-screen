import npyscreen

class MainApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

# This form class defines the display that will be presented to the user.

class MainForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleText, name = "Welcome to DM-Screen!" )

    def afterEditing(self):
        self.parentApp.setNextForm(None)

if __name__ == '__main__':
    App = MainApplication()
    App.run()