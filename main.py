from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# The next three lines are a path operation. Other frameworks call it routes
@app.get("/") # This is the decorator
def root():
    return {"message": "Hello World!"}

@app.get("/posts")
def get_posts():
    return {"data":"This your posts"}

@app.post("/posts")
def get_posts(payload: dict = Body(...)):
    print(payload)
    return {"message":"successfully created posts"}