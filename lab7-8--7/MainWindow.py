import tkinter as tk
class MainWindow(tk.Tk):
    def __init__(self, *arg, **kwarg):
        super(MainWindow, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0); # переменные, ассоциированные с виджетами
        self.principal = None
        self.rate = None
        self.years = None
        self.amount = None
        self.app.mainloop()