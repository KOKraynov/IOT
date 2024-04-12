import copy
from tkinter import Tk
import config
#Библиотеки для анализа и визуализации
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from ErrorWindow import ErrorWindow
class GraphWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.data = np.array(config.data)
        self.point1 = None
        self.point2 = None
        self.point1Bool = True
        self.drawLine = None
        self.drawLineBool = False
        self.point1Scatter = None
        self.point2Scatter = None
        self.canvas = None
        if (self.data.shape[0]==0):
            ErrorWindow(self, config.errorData)
        else:
            if (self.data.shape[1] != 3):
                ErrorWindow(self, config.errorDataImport)
            else:
                self.graph()
    def graph(self):
        # figure, которая включает в себя plot
        fig = Figure(figsize=(5, 5), dpi=100)
        # Добавление subplot
        self.plot1 = fig.add_subplot(111)
        # Изобразить scatter
        self.s = 10
        x = self.data[:, 0].flatten()
        y = self.data[:, 1].flatten()
        colors = [self.data[:, 2].flatten()]
        scatter = self.plot1.scatter(x, y, c=colors, s=self.s, cmap='viridis')
        # создать легенду с уникальными цветами из scatter
        legend1 = self.plot1.legend(*scatter.legend_elements(), loc="upper right", title="R")
        self.plot1.add_artist(legend1)
        # Создание Tkinter canvas
        # включение в нее Matplotlib figure
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.mpl_connect('button_press_event', self.onpick)
        # размещение the Tkinter window
        self.canvas.get_tk_widget().pack()
        # создание Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        # размещение toolbar в Tkinter window
        self.canvas.get_tk_widget().pack()