from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
app = FastAPI()

@app.get('/')
async def root():
    app.mount('/', StaticFiles(directory='dist', html=True),name="static")

if __name__ == '__main__':
    uvicorn.run(app, host="151.243.95.210", port=80)