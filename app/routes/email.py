
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import signup
from passlib.context import CryptContext


# Create an instance of APIRouter to define routes for this specific API section
route = APIRouter()

# Create an instance of Jinja2Templates to handle rendering HTML templates
html = Jinja2Templates(directory="Templates")


route.mount("/project", StaticFiles(directory="project"), name="project")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Route to display the email changing form
@route.get("/changepassword")
def email(request: Request):
    return html.TemplateResponse("PasswordChange.html", {"request": request})

# Route to handle password change submission
@route.post("/changepassword")
def change(request: Request, email: str = Form(...), password: str = Form(), confirm: str = Form(...)):
    result = signup.find_one({"email": email})

    if result:
        # Check if password and confirm_password match
        if password == confirm:
                pw = pwd_cxt.hash(password)
                # Update password for the given email
                signup.update_one({"email": email}, {"$set": {"password": pw, "confirmpassword": confirm}})
                # Redirect to login page with success message
                return html.TemplateResponse("login.html", {"request": request, "message": "Password updated successfully"})
    # Redirect to the emailget page with an error message
    return html.TemplateResponse("PasswordChange.html", {"request": request, "message": "Invalid email"})




