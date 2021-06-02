from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Union
from starlette.exceptions import HTTPException



class Exception_500(Exception):
    def __init__(self,data={},code = 0,message="internal error"):
        self.content={
            'code': code,
            'message': message,
            'data': data
        }

class Exception_401(Exception):
    def __init__(self,data={},code = 0,message="tooken invalid"):
        self.content={
            'code': code,
            'message': message,
            'data': data
        }
# 注意有个 * 号 不是笔误， 意思是调用的时候要指定参数 e.g.resp_200（data=xxxx)
def resp_ok(*, data: Union[list, dict, str],message = "Success",code = 1) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': code,
            'message': message,
            'data': data
        }
    )