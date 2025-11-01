f# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True}

@app.get("/hello")
def hello():
    return {"message": "hello from ASRS mock API"}
