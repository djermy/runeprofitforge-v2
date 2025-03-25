from fastapi import FastAPI

from .store.store import store

app = FastAPI()

@app.on_event("startup")
def on_startup():
    store.create_db_and_tables()

@app.get("/")
async def root():
    return {"hello": "world"}