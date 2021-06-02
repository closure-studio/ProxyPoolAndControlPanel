import proxy
import requests


class Config():
    def __init__(self) -> None:
        self.nodeName = None
        self.publicAddress = '0.0.0.0'
        self.port = 10086
        self.host = '0.0.0.0'
        self.domain = ""
        self.setNodeName()
        self.setDomain()
        self.getPublicAddress()
        self.isIPvaild()
        self.isPortVaild()

        pass

    def getPublicAddress(self) -> None:
        self.publicAddress = requests.get(
            'https://checkip.amazonaws.com').text.strip()
        return

    def setNodeName(self) -> None:
        while True:
            nodeName = input("请输入您的节点名称 \n")
            r = input(f'节点名称 {nodeName} 按任意键进行确认 n 键进行重新输入 \n')
            if r.lower() == 'n':
                continue
            self.nodeName = nodeName
            return

    def isIPvaild(self) -> None:
        while True:
            print(f"当前 IP 地址 为 {self.publicAddress} \n")
            result = input(f"输入任意键 进行 确认 输入 N 进行 人工指定 \n")
            if result.lower() == 'n':
                self.publicAddress = input("请输入IP地址 \n")
                continue
            return

    def isPortVaild(self) -> None:
        while True:
            print(f"当前 端口 地址 为 {self.port} \n")
            result = input(f"输入任意键 进行 确认 输入 N 进行 人工指定 \n")
            if result.lower() == 'n':
                self.port = input("请输入IP地址 \n")
                continue
            return

    def setDomain(self) -> None:
        while True:
            print(f"当前 域名 为 {self.domain} \n")
            result = input(f"输入任意键 进行 确认 输入 N 进行 人工指定 \n")
            if result.lower() == 'n':
                self.domain = input("请输入域名 \n")
                continue
            return

    def nodeRegister(self) ->None:
        r = requests.post("http://34.123.224.81:8000/")

if __name__ == '__main__':
    g = Config()



    proxy.main(['--hostname', '0.0.0.0', '--port',str(g.port),'--basic-auth','arknights:ghYDmaf00HiP'])
