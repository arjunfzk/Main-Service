from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi import Request
from pydantic import BaseModel
from extract import *
import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage


@app.post("/custompage")
async def demo_get(request: Request):
    driver=createDriver()
    url = (await request.json())['url']
    homepage = getCustomHomepage(driver,url)
    driver.close()
    return homepage


@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    


