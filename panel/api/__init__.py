from fastapi import FastAPI, Request
from starlette.status import HTTP_401_UNAUTHORIZED
from panel.api.router import node
from panel.api.router.response import *
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(node.router, prefix='/node', tags=["node"])


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content={
                            'code': 400,
                            'message': '内部错误',
                            'data': str(exc)
                        })

@app.exception_handler(Exception_500)
async def unicorn_exception_handler(request: Request, exc: Exception_500):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=exc.content)

@app.exception_handler(Exception_401)
async def unicorn_exception_handler(request: Request, exc: Exception_401):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                        content=exc.content)
