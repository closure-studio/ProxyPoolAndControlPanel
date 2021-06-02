import requests
import json

from requests.api import patch
from client.config.RootData import RootData
class Config():
    def __init__(self) -> None:
        self.info = {}

        self.info['name'] = None
        self.info["publicAddress"] = '0.0.0.0'
        self.info["port"] = 10086
        self.host = '0.0.0.0'
        self.start()

        pass

    def start(self):
        result = self.readFile()
        if result == True:
            #first time running
            self.setNodeName()
            self.getPublicAddress()
            self.isIPvaild()
            self.isPortVaild()
            self.nodeRegister()
        if result == False:
            self.nodeRegister()



    def readFile(self):
        RootData.load(path='client/config/Root.DataStore')
        info = RootData.get("info")
        if info == None:
            return True
        self.info = info
        return False


    def getPublicAddress(self) -> None:
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
        self.info['publicAddress'] = ip
        return

    def setNodeName(self) -> None:
        while True:
            nodeName = input("请输入您的节点名称 \n")
            r = input(f'节点名称 {nodeName} 按任意键进行确认 n 键进行重新输入 \n')
            if r.lower() == 'n':
                continue
            self.info["nodeName"] = nodeName
            return

    def isIPvaild(self) -> None:
        while True:
            ip = self.info["publicAddress"]
            print(f"当前 IP 地址 为 {ip} \n")
            result = input(f"输入任意键 进行 确认 输入 N 进行 人工指定 \n")
            if result.lower() == 'n':
                self.info["publicAddress"] = input("请输入IP地址 \n")
                continue
            return

    def isPortVaild(self) -> None:
        while True:
            prot = self.info["port"]
            print(f"当前 端口 地址 为 {str(prot)} \n")
            result = input(f"输入任意键 进行 确认 输入 N 进行 人工指定 \n")
            if result.lower() == 'n':
                port = input("请输入IP地址 \n")
                self.info["port"] = port
                continue
            return

    def nodeRegister(self) -> None:
        data = {
            "name": self.info['name'],
            "publicAddress": self.info['publicAddress'],
            "port": self.info['port'],
            "auth": "kMJIK5EyrMCJAd9sftcxf0DnJ3winqtj"
        }
        if 'ID' in self.info.keys():
            data['ID'] = self.info['ID']
        r = requests.post("http://ak-proxypool-panel.nai-ve.com/node/nodeRegister",json=data)
        if r.status_code == 200:
            self.info = json.loads(r.text)["data"]
            RootData.set('info',self.info)
            RootData.dump(save_path='client/config/Root.DataStore')


