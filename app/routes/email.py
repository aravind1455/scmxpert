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

# Route to display the email changing
@route.get("/changepassword")
def email(request: Request):
    return html.TemplateResponse("emailget.html", {"request": request})

# Route to display the email changing
@route.post("/changepassword")
def change(request: Request,email:str = Form(...),password : str = Form(),confirm:str = Form(...)):
    result = signup.find_one({"email": email})
    if result:
        # Check if password and confirm_password match
        if password == confirm:
            # Update password for the given email
            signup.update_one({"email": email}, {"$set": {"password": password,"confirmpassword":confirm}})
            return html.TemplateResponse("login.html", {"request": request,"message": "Password updated successfully"})
    return html.TemplateResponse("emailget.html", {"request": request})



