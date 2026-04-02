import npyscreen

from ui import top, create, load

class MainApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", top.TopMenu())
        self.registerForm("CREATE", create.CreateMenu())
        self.registerForm("LOAD", load.LoadMenu())


if __name__ == '__main__':
    App = MainApplication()
    App.run()