from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import main  # main.calcを使用
import random
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

IMAGE_DIR = "images"  # imagesフォルダをプロジェクト直下に置く

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    context = {
        "request": request,
        "result": None,
        "image_path": None,
        "yen10000": "",
        "yen5000": "",
        "yen1000": "",
        "yen500": "",
        "yen100": "",
        "yen50": "",
        "yen10": "",
        "yen5": "",
        "yen1": "",
        "flag": False
    }
    return templates.TemplateResponse("index.html", context)

@app.post("/", response_class=HTMLResponse)
async def form_post(
    request: Request,
    yen10000: int = Form(0),
    yen5000: int = Form(0),
    yen1000: int = Form(0),
    yen500: int = Form(0),
    yen100: int = Form(0),
    yen50: int = Form(0),
    yen10: int = Form(0),
    yen5: int = Form(0),
    yen1: int = Form(0),
    flag: bool = Form(False)
):
    result = main.calc(
        _10000=yen10000,
        _5000=yen5000,
        _1000=yen1000,
        _500=yen500,
        _100=yen100,
        _50=yen50,
        _10=yen10,
        _5=yen5,
        _1=yen1,
        flag=flag
    )

    image_path = None
    if result == "アイス":
        images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png','.jpg','.jpeg','.gif'))]
        if images:
            image_path = f"/{IMAGE_DIR}/{random.choice(images)}"

    context = {
        "request": request,
        "result": None if image_path else result,
        "image_path": image_path,
        "yen10000": yen10000,
        "yen5000": yen5000,
        "yen1000": yen1000,
        "yen500": yen500,
        "yen100": yen100,
        "yen50": yen50,
        "yen10": yen10,
        "yen5": yen5,
        "yen1": yen1,
        "flag": flag
    }
    return templates.TemplateResponse("index.html", context)

# staticで画像を配信
from fastapi.staticfiles import StaticFiles
app.mount("/images", StaticFiles(directory=IMAGE_DIR), name="images")
