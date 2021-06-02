from panel.api.router.templated import nodeRegister
from panel.config.RootData import RootData
import time
import requests
import threading
class nodeData():
    def __init__(self) -> None:
        self.nodeList = {}
        self.readFile()
        self.healthCheckStart()
        pass


    def healthCheckStart(self):
        nodeCheck = threading.Thread(target=self.healthCheck)
        nodeCheck.name = "Health Check Thread"
        nodeCheck.start()

    def healthCheck(self) -> None:
        while True:
            time.sleep(30)
            for _,node in enumerate(self.nodeList):
                nodeCheck = threading.Thread(target=self.nodeCheck,args=(node,))
                nodeCheck.name = f"nodecheck : {node.ID}"
                nodeCheck.start()

    def nodeCheck(self,node:nodeRegister) ->None:
        if node.publicAddress is None or node.publicAddress == "":
            self.nodeList[node.ID].status = 0
        if node.port is None or node.port == "":
            self.nodeList[node.ID].status = 0

        ulr = f"https://arknights:ghYDmaf00HiP@{node.publicAddress}:{node.port}"
        proxies = {
        'https': ulr
        }
        r = requests.get('https://www.google.com', proxies=proxies)
        if r.status_code == 200:
            self.nodeList[node.ID].status = 0
            self.nodeList[node.ID].lastUpdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if r.status_code != 200:
            self.nodeList[node.ID].status = 1

    def readFile(self):
        RootData.load()
        self.nodeList = RootData.get("nodeList")
        if self.nodeList == None:
            self.nodeList = {}
            RootData.set("nodeList", self.nodeList)
            RootData.dump()
        return

    def saveFile(self):
        RootData.set("nodeList", self.nodeList)
        RootData.dump()

    def setIndex(self,node : nodeRegister):
        index = 0
        indexList = [key for key in self.nodeList.keys()]
        if node.ID is None:
            for i in indexList:
                if index != i:
                    node.ID = index
                    return

    def nodeApend(self,node : nodeRegister) ->None:
        self.setIndex(node)
        self.nodeList[node.ID] = node
        self.saveFile()
        return node

    def getNodeByIndex(self,index):
        if index in self.nodeList.keys():
            return self.nodeList[index]
        return None

    def delNodeByIndex(self,index):
        if index in self.nodeList.keys():
            self.nodeList.pop(index)
        self.saveFile()

nodedata = nodeData()