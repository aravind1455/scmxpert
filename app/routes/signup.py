from fastapi import APIRouter, HTTPException,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import *  
from passlib.context import CryptContext
route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@route.get("/signup")

def sign(request: Request):
    return html.TemplateResponse("signup.html", {"request": request})

@route.post("/signup")
def sign(request: Request,username:str = Form(...),email:str = Form(...),role:str=Form("user"),password:str = Form(...),confirm:str = Form(...)):
    try:
        existing_user = signup.find_one({"username": username})  # db query
        # Check if the email is already registered
        existing_email = signup.find_one({"email":email})  # db query
        if existing_user:
            raise HTTPException(
                status_code=400, detail="Username already used")
        if existing_email:
            raise HTTPException(
                status_code=400, detail="Email already registered")
        # Confirm pass
        if password != confirm:
            raise HTTPException(status_code=400, detail="Passwords do not match")
    except HTTPException as http_error:
        if http_error.detail == "Email already registered":
            raise HTTPException(status_code=400, detail=http_error.detail)
        if http_error.detail == "Passwords do not match":
            raise HTTPException(status_code=400, detail=http_error.detail)
        raise http_error  
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}")
    
    pw = pwd_cxt.hash(password)

    signupdata={
        "user":username,
        "email":email,
        "role":role,
        "password":pw,
        "confirmpassword":confirm
    }
    signup.insert_one(signupdata)
    return html.TemplateResponse("signup.html", {"request": request})