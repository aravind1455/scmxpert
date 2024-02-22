
from fastapi import APIRouter, Form, Request,Depends,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from config.config import signup
from passlib.context import CryptContext
from routes.Jwt_Token import get_current_user



# Create an instance of APIRouter to define routes for this specific API section
route = APIRouter()

# Create an instance of Jinja2Templates to handle rendering HTML templates
html = Jinja2Templates(directory="Templates")


route.mount("/project", StaticFiles(directory="project"), name="project")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Route to display the email changing form
@route.get("/changepassword")
def email(request: Request):
    return html.TemplateResponse("ForgetPassword.html", {"request": request})




@route.post("/changepassword")
def change(request: Request, email: str = Form(...), password: str = Form(), confirm: str = Form(...)):
    try:
        result = signup.find_one({"email": email})

        if result:
            # Check if password and confirm_password match
            if password == confirm:
                pw = pwd_cxt.hash(password)
                # Update password for the given email
                signup.update_one({"email": email}, {"$set": {"password": pw, "confirmpassword": confirm}})
                # Redirect to login page with success message
                return html.TemplateResponse("Login.html", {"request": request, "message": "Password updated successfully"})
        # Redirect to the emailget page with an error message
        return html.TemplateResponse("ForgetPassword.html", {"request": request, "message": "Invalid email"})
    except Exception as e:
        # Handle other exceptions with a 500 status code
        return JSONResponse(content={"detail": str(e)}, status_code=500)
    


@route.get("/changepassword1")
def email(request: Request):
    return html.TemplateResponse("PasswordChange.html", {"request": request})
    


@route.post("/changepassword1")
def change(request: Request, email: str = Form(...), password: str = Form(...), confirm: str = Form(...), token: str = Depends(get_current_user)):
    try:
        if not token:
            raise HTTPException(status_code=401, detail="Unauthorized")

        result = signup.find_one({"email": email})
        if not result:
            raise HTTPException(status_code=400, detail="Invalid email")

        elif result["email"] != token["email"]:
            raise HTTPException(status_code=403, detail="You are not authorized to change this password")

        elif password != confirm:
            raise HTTPException(status_code=400, detail="Passwords do not match")

        pw = pwd_cxt.hash(password) 
        signup.update_one({"email": email}, {"$set": {"password": pw, "confirmpassword": confirm}})
        return JSONResponse(content={"message": "Password updated successfully"}, status_code=200)

    except HTTPException as http_error:
        return JSONResponse(content={"message": http_error.detail}, status_code=http_error.status_code)

    except Exception as e:
        return JSONResponse(content={"message": "Internal server error", "error": str(e)}, status_code=500)






