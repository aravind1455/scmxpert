from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import signup
from passlib.context import CryptContext
from models.models import Signup


route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")



@route.get("/signup")
def sign(request: Request):
    return html.TemplateResponse("SignupPage.html", {"request": request})

@route.post("/signup")
def sign(request: Request, username: str = Form(...), email: str = Form(...), role: str = Form("user"),
         password: str = Form(...), confirm: str = Form(...)):
    existing_user = signup.find_one({"user": username})  # db query
    existing_email = signup.find_one({"email": email}) 
    # print(existing_email,existing_user) # db query
    try:
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already used")
        if existing_email:
            raise HTTPException(status_code=400, detail="email already used")
        if password != confirm:
            raise HTTPException(status_code=400, detail="Passwords does not match")
        if not password[0].isupper():
            raise HTTPException(status_code=400, detail="Password should start with a capital letter")
        if len(password) < 7:
            raise HTTPException(status_code=400, detail="Password should be at least 7 characters long")
        if not any(char.isdigit() for char in password):
            raise HTTPException(status_code=400, detail="Password should contain at least one digit")
    except HTTPException as http_error:
         return html.TemplateResponse("SignupPage.html", {"request": request, "error_message": http_error.detail})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    pw = pwd_cxt.hash(password)
    signup1=Signup(user=username, email=email,role=role,password=pw,confirmpassword=pw)

    
    signup.insert_one(dict(signup1))
    return html.TemplateResponse("SignupPage.html", {"request": request,"success_message": "User registered successfully"})
  
