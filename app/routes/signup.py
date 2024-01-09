from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import *  

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")


@route.get("/signup")
def sign(request: Request):
    return html.TemplateResponse("signup.html", {"request": request})

@route.post("/signup")
def sign(request: Request,username:str = Form(...),email:str = Form(...),role:str=Form("user"),password:str = Form(...),confirm:str = Form(...)):
    signupdata={
        "user":username,
        "email":email,
        "role":role,
        "password":password,
        "confirmpassword":confirm
    }
    signup.insert_one(signupdata)
    return html.TemplateResponse("signup.html", {"request": request})