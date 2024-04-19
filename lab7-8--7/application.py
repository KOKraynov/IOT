# This is a sample Python script.
import os
import sys
import tkinter
from MainWindow import MainWindow
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
app = tkinter.Tk()
path = os.path.join(os.path.dirname(__file__), "images/")
if sys.platform.startswith("win"):
    icon = path + "interest.ico"
else:
    icon = "@" + path + "interest.xbm"
app.iconbitmap(icon)
app.geometry('300x200+600+400')
app.title("Ростовщик")
window = MainWindow(app)
app.protocol("WM_DELETE_WINDOW", window.quit)
app.mainloop()