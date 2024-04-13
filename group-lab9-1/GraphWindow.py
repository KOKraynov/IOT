import copy
from tkinter import Tk
import tkinter as tk
import config
#Библиотеки для анализа и визуализации
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from ErrorWindow import ErrorWindow
import EpuraWindow as ew
class GraphWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.data = np.array(config.data)
        self.title="Визуализация"
        self.button1 = tk.Button(self, text = 'Эпюра', width = 25, command = self.epura_window)
        self.button1.pack(fill="both", expand=1)
        self.point1 = None
        self.point2 = None
        self.point1Bool = True
        self.drawLine = None
        self.drawLineBool = False
        self.point1Scatter = None
        self.point2Scatter = None
        self.canvas = None
        self.line_start = None
        self.points = None
        if (self.data.shape[0]==0):
            ErrorWindow(self, config.errorData)
        else:
            if (self.data.shape[1] != 3):
                ErrorWindow(self, config.errorDataImport)
            else:
                self.graph()

    def epura_window(self):
        self.app = ew.EpuraWindow()
        self.app.mainloop()
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
        self.canvas.get_tk_widget().pack(fill="both", expand = 1)
        # создание Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        # размещение toolbar в Tkinter window
        self.canvas.get_tk_widget().pack()
    def onpick(self, event):
        x, y = event.xdata, event.ydata
        if not self.line_start:
            self.line_start = (x, y)
        else:
            x_origin, y_origin = self.line_start
            self.line_start = None
            self.plot1.plot([x_origin, x], [y_origin, y], 'black', lw=1)
            self.points = []
            for i in range(1, 19, 1):
                x0=x_origin+(x-x_origin)*i/19
                y0=y_origin+(y-y_origin)*i/19
                self.points.append([x0, y0])
                config.interpolatePoints.append([x0, y0])
                self.plot1.plot(x0, y0, 'or')
            self.canvas.draw()
