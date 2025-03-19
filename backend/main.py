from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")

@app.get("/")
async def root():
    return {"hello": "world"}