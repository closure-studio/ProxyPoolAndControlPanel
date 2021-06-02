from fastapi import APIRouter
from panel.api.router.templated import nodeRegister,delNode,getNodes
from panel.api.models.node import nodeRegister as nr
from panel.api.models.node import getNodes as gn
from panel.api.models.node import nodeDel
from panel.api.router.response import *
router = APIRouter()


@router.post("/nodeRegister",summary="节点注册")
async def nodeRegister(node:nodeRegister):
    if node.auth != "kMJIK5EyrMCJAd9sftcxf0DnJ3winqtj":
        return Exception_401()
    node = nr(node)
    return resp_ok(data=node,message = "nodeInfo")


@router.post("/getNodes",summary="获取所有节点")
async def getNodes(node:getNodes):
    if node.auth != "kMJIK5EyrMCJAd9sftcxf0DnJ3winqtj":
        return Exception_401()
    data = gn()
    return resp_ok(data=data,message = "所有节点")


@router.post("/delNodeByIndex",summary="删除节点")
async def delNodeByIndex(node:delNode):
    if node.auth != "kMJIK5EyrMCJAd9sftcxf0DnJ3winqtj":
        return Exception_401()
    data = nodeDel(node)
    return resp_ok(data=data,message = "删除节点")