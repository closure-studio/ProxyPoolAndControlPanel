
import uvicorn
from panel.config.RootData import RootData
from panel.api import app



def init():
    RootData.load()





if __name__ == '__main__':
    init()
    uvicorn.run(app,
                host="0.0.0.0",
                port=8000)