from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")

@route.get("/calculator")
def sign(request: Request):
        return html.TemplateResponse("Calculator.html", {"request": request})