from fastapi import APIRouter, Depends, HTTPException,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import get_current_user

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")


@route.get("/dashboard")
def sign(request: Request):
    return html.TemplateResponse("dasboard.html", {"request": request})
