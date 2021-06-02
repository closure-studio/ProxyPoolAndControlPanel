from panel.api.router.templated import nodeRegister,delNode
from panel.data.data import nodedata


def nodeRegister(node : nodeRegister):
    node = nodedata.nodeApend(node)
    return node.dict()

def nodeDel(node : delNode):
    nodedata.delNodeByIndex(node.ID)
    return None

def getNodes():
    data = {key:val.dict() for key,val in nodedata.nodeList.items()}
    return data