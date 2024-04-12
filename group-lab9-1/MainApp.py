import tkinter as tk
from load_csv_file import load_file as lf
class MainApp(tk.Tk):
#Класс создания основного окна
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.count = 2
        self.button1 = tk.Button(self, text = 'Выбрать файл', width = 25, command = self.load_file)
        self.button1.pack(fill="both", expand=1)
        self.button2 = tk.Button(self, text = 'Визуализация', width = 25, command = self.new_info_window)
        self.button2.pack(fill="both", expand=1)
    def new_info_window(self):
        InfoWindow(self, "Информация о программе")
    def load_file(self):
       lf(self)
    def new_window(self):
        self.app = Demo2()
        self.app.title("Окно № " + str(self.count))
        self.count += 1
        self.app.geometry('300x100+200+100')
        self.app.mainloop()
class InfoWindow():
# Класс создания информационного окна
    def __init__(self, root, label):
        self.top = tk.Toplevel(root)
        self.top.geometry('200x50')
        self.label = tk.Label(self.top, text=label).pack()
        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()
class Demo2(tk.Tk):
# Класс создания нового окна
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.quitButton = tk.Button(self, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
    def close_windows(self):
        self.destroy()
    def main():
        app = Demo1()
        app.title("Окно визуализации")
        app.geometry('300x200+200+100')
        app.mainloop()
    if __name__ == '__main__':
        main()