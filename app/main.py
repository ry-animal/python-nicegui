import uvicorn
from fastapi import FastAPI

from app.front import init

app = FastAPI()

init(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)