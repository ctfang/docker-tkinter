import tkinter as tk


class images(tk.LabelFrame):
    title = "镜像管理"

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master,kw)