import tkinter as tk


class container(tk.LabelFrame):
    title = "容器管理"

    def __init__(self, master=None, **kw):
        super().__init__(master, kw)
