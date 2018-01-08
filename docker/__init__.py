import os
import json

class images(object):
    @staticmethod
    def list():
        titleList = []
        newList = []
        images = os.popen("docker images")
        listData = images.readlines()
        firstStr = True
        listData[0] = listData[0].replace('IMAGE ID', 'IMAGE_ID')
        tempList = list(listData[0])
        for key in range(len(tempList)):
            if tempList[key] == ' ':
                firstStr = True
            elif firstStr == True:
                firstStr = False
                titleList.append({'start': key})

        endKey = len(titleList) - 1
        for key in range(len(titleList)):
            if key == endKey:
                titleList[key]['end'] = -1
                titleList[key]['value'] = listData[0][titleList[key]['start']:titleList[key]['end']].rstrip()
            else:
                titleList[key]['end'] = titleList[key + 1]['start'] - 1
                titleList[key]['value'] = listData[0][titleList[key]['start']:titleList[key]['end']].rstrip()

        del listData[0]
        for str in listData:
            dictData = {}
            for title in titleList:
                dictData[title['value']] = str[title['start']:title['end']].strip()
            newList.append(dictData)
            del dictData

        return newList

    def del_image(self,images_id):
        os.popen("docker rmi "+images_id)

    def image_info(self, id):
        str = "docker inspect "+id
        str = os.popen(str).read()
        dict = json.loads(str)
        return dict[0]

class container():
    @staticmethod
    def all():
        titleList = []
        newList = []
        images = os.popen("docker ps -a")
        listData = images.readlines()
        firstStr = True
        listData[0] = listData[0].replace('CONTAINER ID', 'CONTAINER_ID')
        tempList = list(listData[0])
        for key in range(len(tempList)):
            if tempList[key] == ' ':
                firstStr = True
            elif firstStr == True:
                firstStr = False
                titleList.append({'start': key})

        endKey = len(titleList) - 1
        for key in range(len(titleList)):
            if key == endKey:
                titleList[key]['end'] = -1
                titleList[key]['value'] = listData[0][titleList[key]['start']:titleList[key]['end']].rstrip()
            else:
                titleList[key]['end'] = titleList[key + 1]['start'] - 1
                titleList[key]['value'] = listData[0][titleList[key]['start']:titleList[key]['end']].rstrip()

        del listData[0]
        for str in listData:
            dictData = {}
            for title in titleList:
                dictData[title['value']] = str[title['start']:title['end']].strip()
            newList.append(dictData)
            del dictData

        return newList

    @staticmethod
    def running():
        titleList = []
        newList = []
        images = os.popen("docker ps -a --filter \"status=running\"")
        listData = images.readlines()
        firstStr = True
        listData[0] = listData[0].replace('CONTAINER ID', 'CONTAINER_ID')
        tempList = list(listData[0])
        for key in range(len(tempList)):
            if tempList[key] == ' ':
                firstStr = True
            elif firstStr == True:
                firstStr = False
                titleList.append({'start': key})

        endKey = len(titleList) - 1
        for key in range(len(titleList)):
            if key == endKey:
                titleList[key]['end'] = -1
                titleList[key]['value'] = listData[0][titleList[key]['start']:titleList[key]['end']].rstrip()
            else:
                titleList[key]['end'] = titleList[key + 1]['start'] - 1
                titleList[key]['value'] = listData[0][titleList[key]['start']:titleList[key]['end']].rstrip()

        del listData[0]
        for str in listData:
            dictData = {}
            for title in titleList:
                dictData[title['value']] = str[title['start']:title['end']].strip()
            newList.append(dictData)
            del dictData

        running = []
        for data in newList:
            status = data['STATUS'].find('Up')
            if status != -1:
                running.append(data)
        return running

    @staticmethod
    def title():
        images = os.popen("docker ps -a")
        listData = images.readlines()
        listData = listData[0].replace('CONTAINER ID', 'CONTAINER_ID')
        return tuple(listData.split())

    @staticmethod
    def titleKeyToName(key):
        if key == "CONTAINER_ID":
            return "容器id"
        elif key == "IMAGE":
            return "镜像"
        elif key == "COMMAND":
            return "命令"
        elif key == "CREATED":
            return "创建时间"
        elif key == "STATUS":
            return "状态"
        elif key == "PORTS":
            return "端口"
        elif key == "NAMES":
            return "名称"
        return key


    @staticmethod
    def getIp(CONTAINER_ID):
        str = "docker inspect "+CONTAINER_ID
        str = os.popen(str).read()
        dict = json.loads(str)
        return dict[0]['NetworkSettings']['Networks']['self_default']['IPAddress']
