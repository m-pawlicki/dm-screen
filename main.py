import npyscreen
from utils import db
from ui import top, create, load, list

class MainApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.database = db.CharacterDatabase()
        self.registerForm("MAIN", top.TopMenu())
        self.registerForm("CREATE", create.CreateMenu())
        self.registerForm("LOAD", load.LoadMenu())
        self.registerForm("LIST", list.ListMenu())


if __name__ == '__main__':
    App = MainApplication()
    App.run()