from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True}

@app.get("/hello")
def hello():
    return {"message": "hello from ASRS mock API"}

#@app.post("/task")
#def create_retrieve_task():
    #if DAE requests replenishment
    # take payload from DAE on needs
    # pass the to the ASRS
    # return status code 202 that the ASRS has accpeted the request