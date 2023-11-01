from fastapi import FastAPI
from src.routes import item

app = FastAPI()

app.include_router(item.router, prefix="/item", tags=["item"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
