from panel.api.router.templated import nodeRegister,delNode
from panel.data.data import nodedata


def nodeRegister(node : nodeRegister):
    node = nodedata.nodeApend(node)
    return node

def nodeDel(node : delNode):
    nodedata.delNodeByIndex(node.ID)
    return None

def getNodes():
    data = nodedata.nodeList
    return data