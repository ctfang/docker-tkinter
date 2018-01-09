import tkinter as tk
import tkinter.messagebox
import docker
from window.Tableview import Tableview
from window.create_container import create


class images(tk.Frame):
    title = "镜像管理"
    left_width = 150

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master,cnf, **kw)
        left_label = tk.Frame(self, width=self.left_width)
        left_label.pack(fill=tk.Y, side=tk.LEFT)

        self.opent_right_label()

        tk.Button(left_label, text="刷新列表", width=20, command=self.resert_images()).pack()
        tk.Button(left_label, text="下载新镜像", width=20, command=self.down_docker).pack()
        tk.Button(left_label, text="创建容器", width=20, command=self.create_container).pack()
        tk.Button(left_label, text="删除", width=20, command=self.del_image).pack(side=tk.BOTTOM)

    # 打开右边列表
    def opent_right_label(self):
        self.right_label = tk.Frame(self, background='white', width=self.winfo_screenwidth() - self.left_width, padx=0, pady=0)
        self.right_label.pack(fill=tk.Y, side=tk.LEFT)

        images = docker.images.list()

        tableVies = Tableview(self.right_label)
        tableVies.title_check()
        tableVies.title(text='名称', column=1, width='20')
        tableVies.title(text='版本', column=2, width='20')
        tableVies.title(text='大小', column=3, width='20')
        tableVies.title(text='时间', column=4, width='30')

        for data in images:
            tableVies.set_check(data['IMAGE_ID'])
            tableVies.insert(data['REPOSITORY'], data['TAG'], data['SIZE'], data['CREATED'])

        self.tableVies = tableVies
        del tableVies

    # 创建容器
    def create_container(self):
        CheckbuttonValue = self.tableVies.get_check()
        for key in CheckbuttonValue:
            if CheckbuttonValue[key].get()=="1":
                create(key)
                return

        tkinter.messagebox.showinfo(title='提示',message='没有选择镜像')

    # 下载镜像
    def down_docker(self):
        CheckbuttonValue = self.tableVies.get_check()
        for key in CheckbuttonValue:
            print(key, CheckbuttonValue[key].get())

    # 删除镜像
    def del_image(self):
        is_del = tkinter.messagebox.askokcancel('敏感警告','你将删除镜像，是否执行')
        if is_del == False:
            return False
        iamges = docker.images()
        CheckbuttonValue = self.tableVies.get_check()
        for key in CheckbuttonValue:
            if  CheckbuttonValue[key].get()=="1":
                iamges.del_image(key)
        self.resert_images()

    # 重载当前窗口
    def resert_images(self):
        self.right_label.destroy()
        self.opent_right_label()