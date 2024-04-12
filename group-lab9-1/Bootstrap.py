import config
from MainApp import MainApp

class Bootstrap():

    @staticmethod
    def initEnviroment():
        config.mainApp = MainApp()
        config.mainApp.title("Визуализация триангуляционных данных")
        config.mainApp.iconbitmap("test_axe.ico")
        config.mainApp.geometry('400x200+200+100')

    @staticmethod
    def run():
        config.mainApp.mainloop()