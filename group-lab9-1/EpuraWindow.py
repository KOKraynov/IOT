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
from scipy.spatial import Delaunay
from delone_triangulation import delone_triangulation
class EpuraWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.title="Эпюра"
        self.interpolatePoints = np.array(config.interpolatePoints)
        self.canvas = None
        self.points = None
        if (self.interpolatePoints.shape[0]==0):
            ErrorWindow(self, config.errorData)
        else:
            if (self.interpolatePoints.shape[1] != 2):
                ErrorWindow(self, config.errorDataImport)
            else:
                self.graph()
    def graph(self):
        # figure, которая включает в себя plot
        fig = Figure(figsize=(5, 5), dpi=100)
        # Добавление subplot
        self.plot1 = fig.add_subplot(111)
        n = 2
        points = np.array(config.data)[:, :2]
        values=np.array(config.data)[:, 2]
        p_values=[]
        p=np.array(config.interpolatePoints)
        b0=[]
        tri = Delaunay(points)
        s = tri.find_simplex(p)
        v = tri.vertices[s]
        m = tri.transform[s]
        for i in range(len(p)):
            s = m[i, :n, :n]
            s1 = m[i, n, :]
            b0.append(m[i, :n, :n].dot(p[i] - m[i, n, :]))
        b=np.array(b0)
        w = np.c_[b, 1 - b.sum(axis=1)]
        for i in range(len(p)):
            p_values.append( np.inner(values[v[i]], w[i]))
        print(p_values)
        # Изобразить scatter
        #x = self.interpolatePoints[:, 0].flatten()
        #y = self.interpolatePoints[:, 1].flatten()
        p00=[0, 1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        scatter = self.plot1.scatter(p00, p_values, cmap='viridis')
        # Создание Tkinter canvas
        # включение в нее Matplotlib figure
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        # размещение the Tkinter window
        self.canvas.get_tk_widget().pack(fill="both", expand = 1)
        # создание Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        # размещение toolbar в Tkinter window
        self.canvas.get_tk_widget().pack()
