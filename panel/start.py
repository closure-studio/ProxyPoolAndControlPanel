
import uvicorn
from panel.config.RootData import RootData
from panel.api import app





if __name__ == '__main__':

    uvicorn.run(app,
                host="0.0.0.0",
                port=3000,
                log_level = 'error',)