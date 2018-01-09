import tkinter as tk


class version(tk.LabelFrame):
    title = "版本说明"

    version = "版本：RC0.0.1\n作者：明月有色\n版权所有：blog.ctfang.com\n源码地址：github.com/selden1992"

    def __init__(self, master=None, **kw):
        super().__init__(master, kw)

        text = tk.Text(self)
        text.insert(tk.INSERT,self.version)
        text.pack()