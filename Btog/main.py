from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from pathlib import Path
app = FastAPI()
DIST_DIR = Path(__file__).resolve().parent/"dist"

@app.get("/")
async def root():
    app.mount('/', StaticFiles(directory=DIST_DIR, html=True),name="static")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)