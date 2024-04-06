# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import ttk     # подключаем пакет ttk

def readFile():
    f=open("points.csv", "r")
    s=f.readlines()
    data=[]
    x=[]
    y=[]
    r=[]
    for item in s:
        data.append(item.replace("\n",""))
    print(s)
    data.pop(0)
    for item in data:
        item = item.split(",")
        x.append(item[0])
        y.append(item[1])
        r.append(item[2])
    print(data)
    print(max(x), max(y))
root = Tk()  # создаем корневой объект - окно
root.title("Триангуляуия Делоне")  # устанавливаем заголовок окна
root.geometry("300x250")  # устанавливаем размеры окна
def clickBtnFile():
    readFile()
btnFile = ttk.Button(text="Выбрать файл", command=clickBtnFile) # создаем кнопку из пакета ttk
btnFile.pack(expand=True, fill=BOTH)
def clickBtnVisual():
    btnFile["text"] = "Clicks"
    # Новое окно с визуализацией
btnVisual = ttk.Button(text="Визуализация", command=clickBtnVisual) # создаем кнопку из пакета ttk
btnVisual.pack(expand=True, fill=BOTH)

root.mainloop()