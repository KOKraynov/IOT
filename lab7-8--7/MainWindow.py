import tkinter as tk
class MainWindow(tk.Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0);
        # виджеты
        self.principal = tk.DoubleVar()
        self.principal.set(1000.0)
        self.rate = tk.DoubleVar()
        self.principal.set(5.0)
        self.years = tk.IntVar()
        self.amount = tk.StringVar()
        # Инициализация
        principalLabel = tk.Label(self, text="Займ $:", anchor=tk.W, underline=0)
        rateLabel = tk.Label(self, text="Процент %:", anchor=tk.W, underline=0)
        yearsLabel = tk.Label(self, text="Годы:", anchor=tk.W, underline=0)
        amountLabel = tk.Label(self, text="Сумма $:", anchor=tk.W, underline=0)
        actualAmountLabel = tk.Label(self, textvariable=self.amount, relief=tk.SUNKEN, anchor=tk.E)
        principalScale = tk.Scale(self, variable=self.principal, command=self.updateUi,
                                  from_=100, to=10000000, resolution=100, orient=tk.HORIZONTAL)
        rateScale = tk.Scale(self, variable=self.rate, command=self.updateUi,
                             from_=1, to=100, resolution=0.25, digits=5, orient=tk.HORIZONTAL)
        yearsScale = tk.Scale(self, variable=self.years, command=self.updateUi,
                              from_=1, to=50, orient=tk.HORIZONTAL)
        # Разметка
        principalLabel.grid(row=0, column=0, padx=2, ipadx=2, sticky=tk.W)
        principalScale.grid(row=0, column=1, padx=2, ipadx=2, sticky=tk.EW)
        rateLabel.grid(row=1, column=0, padx=2, ipadx=2, sticky=tk.W)
        rateScale.grid(row=1, column=1, padx=2, ipadx=2, sticky=tk.EW)
        yearsLabel.grid(row=2, column=0, padx=2, ipadx=2, sticky=tk.W)
        yearsScale.grid(row=2, column=1, padx=2, ipadx=2, sticky=tk.EW)
        amountLabel.grid(row=3, column=0, padx=2, ipadx=2, sticky=tk.W)
        actualAmountLabel.grid(row=3, column=1, padx=2, ipadx=2, sticky=tk.EW)
        # Фокус
        principalScale.focus_set()
        self.updateUi()
        parent.bind("<Alt-p>", lambda *ignore: principalScale.focus_set())
        parent.bind("<Alt-r>", lambda *ignore: rateScale.focus_set())
        parent.bind("<Alt-y>", lambda *ignore: yearsScale.focus_set())
        parent.bind("<Control-q>", self.quit)
        parent.bind("<Escape>", self.quit)
    def updateUi(self, *ignore):
        amount = self.principal.get() * ((1 + (self.rate.get()/100.0)) ** self.years.get())
        self.amount.set("{0: .2f}".format(amount))
    def quit(self, event=None) -> None:
        self.parent.destroy()
