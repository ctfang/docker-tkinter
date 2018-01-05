import tkinter
from tkinter import ttk


class Tableview:
    def __init__(self, master=None, **kw):
        self.master = master
        self.titleLabel = ttk.Labelframe(self.master)
        self.titleLabel.pack(side=tkinter.TOP, expand=0, fill=tkinter.X)

    def title(self, **config):
        type = config['type']
        if type == "text":
            titleLabel = ttk.Label(self.titleLabel, text='fasfdsa', background="cyan")
            titleLabel.pack()

        elif type == "label":
            print('label')

