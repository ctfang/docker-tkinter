import tkinter as tk
import docker
from window.Tableview import Tableview
import tkinter.messagebox


class running(tk.LabelFrame):
    title = "运行中的容器"
    left_width = 150

    def __init__(self, master=None, **kw):
        super().__init__(master, kw)

        self.left_label = tk.Frame(self, width=self.left_width)
        self.left_label.pack(fill=tk.Y, side=tk.LEFT)

        self.opent_right_label()

        tk.Button(self.left_label, text="刷新列表", width=20, command=self.resert_images).pack()
        tk.Button(self.left_label, text="启动", width=20, command=self.start_docker).pack()
        tk.Button(self.left_label, text="停止", width=20, command=self.stop_docker).pack()

        tk.Button(self.left_label, text="删除", width=20, command=self.del_docker).pack(side=tk.BOTTOM)

    def stop_docker(self):
        CheckbuttonValue = self.tableVies.get_check()
        for key in CheckbuttonValue:
            if CheckbuttonValue[key].get()=="1":
                docker.container.stop(key)
        self.resert_images()

    # 重载当前窗口
    def resert_images(self):
        self.right_label.destroy()
        self.opent_right_label()

    # 打开右边列表
    def opent_right_label(self):
        self.right_label = tk.Frame(self, background='white', width=self.winfo_screenwidth() - self.left_width)
        self.right_label.pack(fill=tk.Y, side=tk.LEFT)

        docker_ps = docker.container.all()

        self.tableVies = Tableview(self.right_label)
        self.tableVies.title_check()
        self.tableVies.title(text='名称', column=1, width='15')
        self.tableVies.title(text='状态', column=2, width='8')
        self.tableVies.title(text='镜像', column=3, width='20')
        self.tableVies.title(text='ip', column=4, width='12')
        self.tableVies.title(text='端口', column=5, width='100')

        for data in docker_ps:
            if data['STATUS'].find('Up')<0:
                status = "off"
            else:
                status = "up"
            ip = docker.container.getIp(data['CONTAINER_ID'])
            self.tableVies.set_check(data['NAMES'])
            self.tableVies.insert(data['NAMES'], status, data['IMAGE'], ip, data['PORTS'])

    def start_docker(self):
        CheckbuttonValue = self.tableVies.get_check()
        for key in CheckbuttonValue:
            if CheckbuttonValue[key].get()=="1":
                docker.container.start(key)
        self.resert_images()

    def del_docker(self):
        is_del = tkinter.messagebox.askokcancel('敏感警告','你将删除实例，是否执行')
        if is_del == False:
            return False
        CheckbuttonValue = self.tableVies.get_check()
        for key in CheckbuttonValue:
            if  CheckbuttonValue[key].get()=="1":
                docker.container.delete(key)
        self.resert_images()