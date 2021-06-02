from typing import Optional,Text
from pydantic import BaseModel




class nodeRegister(BaseModel):
    name : str
    publicAddress : str
    port : str
    auth : str
    domain : Optional[str]
    ID : Optional[int]
    status : Optional[int]
    lastUpdate : Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "name": "测试服务器",
                "publicAddress": "0.0.0.0",
                "port": "10086",
                "domain":"",
                "auth" : "kMJIK5EyrMCJAd9sftcxf0DnJ3winqtj",
                "ID" : 0,
                "status" : 0,
                "lastUpdate" : "",
            }
        }

class getNodes(BaseModel):
    auth : str
    class Config:
        schema_extra = {
            "example": {
                "auth" : "kMJIK5EyrMCJAd9sftcxf0DnJ3winqtj",
            }
        }



class delNode(BaseModel):
    auth : str
    ID : int
    class Config:
        schema_extra = {
            "example": {
                "auth": "kMJIK5EyrMCJAd9sftcxf0DnJ3winqtj",
                "ID" : 0,
            }
        }








