import tkinter
from tkinter import ttk


class Tableview:
    CheckbuttonValue = {}
    title_config = {}
    row = 0

    def __init__(self, master=None, **kw):
        self.master = master
        self.titleLabel = ttk.Frame(self.master, padding='0 0 0 0')
        self.titleLabel.pack(side=tkinter.TOP, expand=0, fill=tkinter.X)

    def title_check(self, **value):
        self.all_check = tkinter.StringVar(value=0)
        value['variable'] = self.all_check
        value['command'] = self.check_all
        ttk.Checkbutton(self.titleLabel, **value).grid(row=0, column=0)

    def title(self, column=1, **value):
        ttk.Label(self.titleLabel, **value).grid(row=0, column=column)
        self.title_config[column] = value

    def insert(self, *values):
        column = 1
        for data in values:
            temp_config = self.title_config[column]
            temp_config['text'] = data
            ttk.Label(self.titleLabel, **temp_config).grid(row=self.row, column=column)
            column = column + 1

    def set_check(self, id):
        self.row = self.row + 1
        self.CheckbuttonValue[id] = tkinter.StringVar(value=0)
        tempLabel = ttk.Checkbutton(self.titleLabel, variable=self.CheckbuttonValue[id])
        tempLabel.grid(row=self.row, column=0)

    def check_all(self):
        if self.all_check.get() == '1':
            for data in self.CheckbuttonValue.values():
                data.set(1)
        else:
            for data in self.CheckbuttonValue.values():
                data.set(0)

    def get_check(self):
        return self.CheckbuttonValue