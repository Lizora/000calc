from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import main
import os, random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# staticフォルダとしてimagesを公開
app.mount("/images", StaticFiles(directory="images"), name="images")

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
        image_dir = os.path.join(os.path.dirname(__file__), "images")
        images = [f for f in os.listdir(image_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
        if images:
            chosen = random.choice(images)
            image_path = f"/images/{chosen}"

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
