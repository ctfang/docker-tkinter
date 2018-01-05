import tkinter as tk
import docker
from window.Tableview import Tableview


class running(tk.LabelFrame):
    title = "运行中的容器"
    CheckbuttonValue = {}

    def __init__(self, master=None, **kw):
        super().__init__(master, kw)

        left_width = 150
        left_label = tk.LabelFrame(self, background='white', width=left_width)
        left_label.pack(fill=tk.Y, side=tk.LEFT)
        right_label = tk.LabelFrame(self, background='white', width=self.winfo_screenwidth() - left_width)
        right_label.pack(fill=tk.Y, side=tk.LEFT)

        docker_ps = docker.container.running()
        docker_data = []
        for data in docker_ps:
            ip = docker.container.getIp(data['CONTAINER_ID'])
            docker_data.append({"NAMES": data['NAMES'], "IMAGE": data['IMAGE'], "PORTS": data['PORTS'], "IP": ip, "CONTAINER_ID":data['CONTAINER_ID']})
        del docker_ps

        tk.Checkbutton(right_label, variable=self.CheckbuttonValue).grid(row=0, column=0)
        tk.Label(right_label, background='white', text='名称', width=12, anchor=tk.W) \
            .grid(row=0, column=1)
        tk.Label(right_label, background='white', text='镜像', width=17, anchor=tk.W) \
            .grid(row=0, column=2)
        tk.Label(right_label, background='white', text='ip', width=14, anchor=tk.W) \
            .grid(row=0, column=3)
        tk.Label(right_label, background='white', text='端口', width=100, anchor=tk.W) \
            .grid(row=0, column=4)

        row = 1
        for data in docker_data:
            self.CheckbuttonValue[data['CONTAINER_ID']] = tk.StringVar(value=1)
            tk.Checkbutton(right_label, variable=self.CheckbuttonValue[data['CONTAINER_ID']]).grid(row=row, column=0)
            tk.Label(right_label, background='white', text=data['NAMES'], width=12, anchor=tk.W)\
                .grid(row=row, column=1)
            tk.Label(right_label, background='white', text=data['IMAGE'], width=17, anchor=tk.W)\
                .grid(row=row, column=2)
            tk.Label(right_label, background='white', text=data['IP'], width=14, anchor=tk.W)\
                .grid(row=row, column=3)
            tk.Label(right_label, background='white', text=data['PORTS'], width=100, anchor=tk.W)\
                .grid(row=row,column=4)
            row = row + 1

        tk.Button(left_label, text="启动", width=20, command=self.start_docker).pack()
        tk.Button(left_label, text="停止", width=20).pack()
        tk.Button(left_label, text="删除", width=20).pack(side=tk.BOTTOM)

    def start_docker(self):
        for data in self.CheckbuttonValue.values():
            print(data.get())

    def check_all(self):
        print(self.CheckbuttonValue)