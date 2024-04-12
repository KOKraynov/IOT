import csv
from tkinter import filedialog
import config
from ErrorWindow import ErrorWindow

def load_file(self):
    # Загрузка csv
    filepath = filedialog.askopenfilename()
    if filepath != "":
        config.data = []
        with open(filepath, encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter=",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == 0:
                    # Проверка количества и содержания столбцов
                    if len(row) != 3:
                        ErrorWindow(self, config.errorTextImport)
                        break
                else:
                    l = []
                    for num in row:
                        l.append(int(num))
                    config.data.append(l)
                count += 1
    else:
        ErrorWindow(self, config.errorTextImport)