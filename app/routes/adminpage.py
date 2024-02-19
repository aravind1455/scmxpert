from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")

# Route to display the dashboard page
@route.get("/adminpage")
def sign(request: Request):
    return html.TemplateResponse("AdminPage.html", {"request": request})