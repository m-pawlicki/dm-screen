import npyscreen

from ui import top, create, load

class MainApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", top.TopMenu())
        self.registerForm("LOAD", create.CreateMenu())
        self.registerForm("CREATE", load.LoadMenu())


if __name__ == '__main__':
    App = MainApplication()
    App.run()