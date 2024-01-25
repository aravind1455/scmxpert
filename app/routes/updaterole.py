from fastapi import APIRouter, HTTPException,Request,Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import *  
from typing import Optional
# Create an instance of APIRouter to define routes for this specific API section
route=APIRouter()
# Create an instance of Jinja2Templates to handle rendering HTML templates
html = Jinja2Templates(directory = "Templates")
# Mount the "project" directory containing static files (e.g., CSS, JS) under the "/project" route
# This allows FastAPI to serve static files directly from the specified directory
route.mount("/project", StaticFiles(directory="project"), name = "project")
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
from routes.login import *

# Route to display the email changing
@route.get("/changerole")
def email(request: Request):
    return html.TemplateResponse("UpdateRole.html", {"request": request})

# Route to display the email changing
from fastapi.responses import JSONResponse

from fastapi.responses import JSONResponse

@route.post("/changeroleuser")
def change(request: Request, user: dict, token: str = Depends(get_current_user)):
    try:
        if token:
            if user:
                result = signup.find_one({"user": user["user"]})
                if result:
                    result1 = signup.update_one({"user": user["user"]}, {"$set": {"role": "admin"}})
                    if result1.modified_count > 0:
                        return JSONResponse(content={"message": "Role updated successfully"}, status_code=200)
                    else:
                        return JSONResponse(content={"message": "User not found"}, status_code=404)
                        # raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")


