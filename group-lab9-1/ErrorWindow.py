import tkinter as tk
class ErrorWindow():
# Класс создания информационного окна
    def __init__(self, root, label):
        self.top = tk.Toplevel(root)
        self.top.geometry('200x50')
        self.label = tk.Label(self.top, text=label).pack()
        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()
