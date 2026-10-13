from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)

# The next three lines are a path operation. Other frameworks call it routes
@app.get("/")  # This is the decorator
def root():
    return {"message": "Hello World!"}
