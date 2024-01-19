from fastapi import APIRouter, HTTPException,Request,Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import *  
# Create an instance of APIRouter to define routes for this specific API section
route=APIRouter()
# Create an instance of Jinja2Templates to handle rendering HTML templates
html = Jinja2Templates(directory = "Templates")
# Mount the "project" directory containing static files (e.g., CSS, JS) under the "/project" route
# This allows FastAPI to serve static files directly from the specified directory
route.mount("/project", StaticFiles(directory="project"), name = "project")
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Route to display the email changing
@route.get("/changerole")
def email(request: Request):
    return html.TemplateResponse("updaterole.html", {"request": request})

# Route to display the email changing
@route.post("/changerole")
def change(request: Request,user:str = Form(...),token : str = Depends(oauth2_scheme)):
    if token:
        if user:
            result = signup.find_one({"user": user})
            if result:
                    result= signup.update_one({"user":user} , {"$set": {"role": "admin"}})
                    return html.TemplateResponse("login.html", {"request": request,"message": "Password updated successfully"})
            return html.TemplateResponse("updaterole.html", {"request": request})