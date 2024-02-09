from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


route = APIRouter()
html = Jinja2Templates(directory="Templates")

# Route to display the dashboard page
@route.get("/Dashboard")
def sign(request: Request):
    return html.TemplateResponse("Dashboard.html", {"request": request})

@route.get("/contact")
def sign(request: Request):
    return html.TemplateResponse("Contact.html", {"request": request})

