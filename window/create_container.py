import tkinter as tk
import docker

class create(tk.Tk):
    w = 1000
    h = 600

    def __init__(self,image):
        super(create, self).__init__()
        name_tag = self.get_tag(image)
        self.title(name_tag)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        self.x = (ws / 2) - (self.w / 2)
        self.y = (hs / 2) - (self.h / 2)
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.mainloop()

    def get_tag(self,image):
        data = docker.images().image_info(image)
        return data['RepoTags'][0]

if __name__ == '__main__':
    create()