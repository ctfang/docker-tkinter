import tkinter.ttk
from config.AppConfig import AppConfig


class Window:
    def __init__(self):
        self.title = AppConfig.get(strKey="title");

    def buildRoot(self):
        self.root = root = tkinter.Tk()
        root.title(self.title);
        root.geometry("800x500+330+180")
        self.buildMainFrame()

    def buildMainFrame(self):
        width_label = 113
        top_frame = tkinter.ttk.Frame(self.root, padding="0 0 0 2")
        top_frame.grid(column=0, row=0)
        top_label = tkinter.Button(top_frame, text="运行中", width=(width_label - 2) // 3, height=2, background='gray')
        top_label.grid(column=0, row=0, padx=0)
        top_label = tkinter.Button(top_frame, text="容器管理", width=(width_label) // 3, height=2, background='gray')
        top_label.grid(column=1, row=0, padx=0)
        top_label = tkinter.Button(top_frame, text="镜像管理", width=(width_label // 3)-1, height=2, background='gray')
        top_label.grid(column=2, row=0, padx=0)
        top_label.bind("<Button-1>", self.display);

        content = tkinter.ttk.Frame(self.root, padding="0 0 0 0")
        content.grid(column=0, row=1)
        content_label = tkinter.Label(content, text="运行中", width=width_label, height=27, background='white')
        content_label.pack()
        self.content_label = content_label

        content_label_2 = tkinter.Label(content, text="停止", width=width_label, height=27, background='white')
        content_label_2.pack()
        content_label_2.forget()
        self.content_label_2 = content_label_2

    def loop(self):
        self.root.mainloop()

    def display(self, event):
        if self.content_label.winfo_viewable():
            self.content_label.forget()
        else:
            self.content_label.pack()
        if self.content_label_2.winfo_viewable():
            self.content_label_2.forget()
        else:
            self.content_label_2.pack()



window = Window()

window.buildRoot()

window.loop()
