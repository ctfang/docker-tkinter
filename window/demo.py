import os
import config
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Notebook
import docker.db as db
import docker


class Timer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(config.title)
        self.geometry(config.geometry)

        self.notebook = Notebook(self)
        running_tab = RunTag(self.notebook)
        images_tab = ImagesTab(self.notebook)

        self.notebook.add(running_tab, text="运行中的容器")
        self.notebook.add(images_tab, text="镜像管理")
        self.notebook.pack(fill=tk.BOTH, expand=1)


class RunTag(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()

        rigth_frame = tk.LabelFrame(self)
        rigth_frame.pack(side=tk.RIGHT, expand=1, fill=tk.X, anchor=tk.N)

        content = tk.LabelFrame(self, background="cyan")
        content.pack(side=tk.RIGHT, expand=0, fill=tk.X)

        docker_ps = docker.container.running()

        tree = ttk.Treeview(content, columns=("NAMES", "IMAGE", "PORTS"), height=18, show="headings")
        tree.heading("NAMES", text=docker.container.titleKeyToName("NAMES"), anchor=tk.W)
        tree.column("NAMES", anchor=tk.W, width=100)
        tree.heading("IMAGE", text=docker.container.titleKeyToName("IMAGE"), anchor=tk.W)
        tree.column("IMAGE", anchor=tk.W, width=180)
        tree.heading("PORTS", text=docker.container.titleKeyToName("PORTS"), anchor=tk.W)
        tree.column("PORTS", anchor=tk.W, width=250)

        for values in docker_ps:
            value = (values["NAMES"], values["IMAGE"], values["PORTS"])
            tree.insert("", tk.END, values=value)
        tree.pack()

        translate_button = tk.Button(rigth_frame, text="开始")
        translate_button.pack(side=tk.TOP, fill=tk.BOTH)
        translate_button = tk.Button(rigth_frame, text="停止")
        translate_button.pack(side=tk.TOP, fill=tk.X)
        translate_button = tk.Button(rigth_frame, text="重启")
        translate_button.pack(side=tk.TOP, fill=tk.X)
        translate_button = tk.Button(rigth_frame, text="删除")
        translate_button.pack(side=tk.BOTTOM, fill=tk.X)


class ImagesTab(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()
        self.italian_copy_button = tk.Button(self, text="Copy to Clipboard", command=self.test())
        self.italian_copy_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.italian_translation = tk.StringVar(self)
        self.italian_translation.set("")

        self.italian_label = tk.Label(self, textvar=self.italian_translation, bg="lightgrey", fg="black")
        self.italian_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def test(self):
        pass


if __name__ == "__main__":
    timer = Timer()

    if not os.path.isfile("docker.db"):
        db.create()

    timer.mainloop()
