import tkinter as tk
from tkinter.filedialog import askdirectory
import docker


class create(tk.Tk):
    w = 1000
    h = 600
    submit = {}
    port_row = 0
    dir_row = 0

    def __init__(self, image):
        super(create, self).__init__()
        self.image_name = self.get_tag(image)
        self.title("创建容器实例 on " + self.image_name)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        self.x = (ws / 2) - (self.w / 2)
        self.y = (hs / 2) - (self.h / 2)
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.handel()
        self.mainloop()

    def handel(self):
        tk.Label(self, text='基础镜像').grid(row=0, column=0, ipadx=20, ipady=20)
        self.submit["image"] = tk.Entry(self)
        self.submit["image"].insert(0, self.image_name)
        self.submit["image"].grid(row=0, column=1, sticky=tk.W)

        tk.Label(self, text='容器名称').grid(row=1, column=0, ipadx=20, ipady=20)
        self.submit["--name"] = tk.Entry(self)
        self.submit["--name"].grid(row=1, column=1, sticky=tk.W)

        # 工作目录
        tk.Label(self, text='工作目录').grid(row=2, column=0, ipadx=20, ipady=20)
        self.submit["--workdir"] = tk.Entry(self)
        self.submit["--workdir"].insert(0, "/")
        self.submit["--workdir"].grid(row=2, column=1, sticky=tk.W)

        # 映射端口
        self.entry_port = tk.LabelFrame(self, text="映射端口")
        self.entry_port.grid(row=3, column=1, sticky=tk.N)
        tk.Label(self.entry_port, text="本机", width=10).grid(row=0, column=0, ipadx=0, ipady=0)
        tk.Label(self.entry_port, text="容器", width=10).grid(row=0, column=1, ipadx=0, ipady=0)
        self.submit["--publish"] = {}
        self.add_entry_port()
        tk.Button(self, text="新增", command=self.add_entry_port).grid(row=4, column=1, ipadx=20, pady=20)

        # 映射目录
        self.entry_dir = tk.LabelFrame(self, text="映射目录")
        self.entry_dir.grid(row=3, column=2, sticky=tk.N)
        tk.Label(self.entry_dir, text="本机", width=10).grid(row=0, column=0, ipadx=0, ipady=0)
        tk.Label(self.entry_dir, text="容器", width=10).grid(row=0, column=1, ipadx=0, ipady=0)
        self.submit["--volume"] = {}
        self.add_entry_dir()
        tk.Button(self, text="新增", command=self.add_entry_dir).grid(row=4, column=2, ipadx=20, pady=20)

        # 提交目录
        tk.Button(self, text='提交', command=self.submit_data).grid(row=5, column=1, ipadx=20, pady=20, sticky=tk.W)

    # 新增目录
    def add_entry_dir(self):
        self.dir_row = self.dir_row + 1
        from_key = "source_" + str(self.dir_row)
        to_key = "to_" + str(self.dir_row)
        temp_entry = tk.Label(self.entry_dir)
        temp_entry.grid(row=self.dir_row, column=0)

        self.submit["--volume"][from_key] = tk.Entry(temp_entry)
        self.submit["--volume"][to_key] = tk.Entry(self.entry_dir)
        self.submit["--volume"][from_key].grid(row=0, column=0)
        tk.Button(temp_entry, text="选择目录", command=lambda: self.select_path(from_key)).grid(row=0, column=1)
        self.submit["--volume"][to_key].grid(row=self.dir_row, column=1)

    # 动态新增端口
    def add_entry_port(self):
        self.port_row = self.port_row + 1
        from_key = "source_" + str(self.port_row)
        to_key = "to_" + str(self.port_row)
        self.submit["--publish"][from_key] = tk.Entry(self.entry_port)
        self.submit["--publish"][to_key] = tk.Entry(self.entry_port)
        self.submit["--publish"][from_key].grid(row=self.port_row, column=0)
        self.submit["--publish"][to_key].grid(row=self.port_row, column=1)

    # 获取路径
    def select_path(self, from_key):
        # 第一步取消置顶
        self.wm_attributes('-topmost', 0)
        path = askdirectory()
        # 选择目录后置顶，显示值
        self.wm_attributes('-topmost', 1)
        self.submit["--volume"][from_key].insert(1, path)

    # 提交数据
    def submit_data(self):
        str_command = ''
        for key in self.submit:
            if isinstance(self.submit[key], dict) == False:
                data = self.submit[key].get()
                if data!='':
                    if key=='image':
                        continue
                    else:
                        str_command = str_command + " " + key + " " + self.submit[key].get()
            else:
                temp = ''
                for key_1 in self.submit[key]:
                    data = self.submit[key][key_1].get()
                    if data == "":
                        temp = ''
                    elif key_1.find('source_') != -1:
                        temp = " " + key + ' ' + data
                    else:
                        temp = temp + ':' + data
                if temp != '':
                    str_command = str_command + " " + temp

        obj_docker = docker.images()
        obj_docker.docker_run(str_command, self.submit['image'].get())
        self.destroy()

    # 获取image版本
    def get_tag(self, image):
        data = docker.images().image_info(image)
        return data['RepoTags'][0]


if __name__ == '__main__':
    create()
