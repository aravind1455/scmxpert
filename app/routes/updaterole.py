from fastapi import APIRouter, HTTPException,Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import * 
from fastapi.responses import JSONResponse 
from routes.login import *

route=APIRouter()

html = Jinja2Templates(directory = "Templates")

route.mount("/project", StaticFiles(directory="project"), name = "project")
# from fastapi.security import OAuth2PasswordBearer
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@route.get("/changerole")
def email(request: Request):
    return html.TemplateResponse("UpdateRole.html", {"request": request})


@route.post("/changeroleuser")
def change(request: Request, user: dict, token: str = Depends(get_current_user)):
    try:
        if token:
            if user:
                result = signup.find_one({"user": user["user"]})
                if result:
                    if  token["role"]=="user":
                         return JSONResponse(content={"message": "sry you are a user"}, status_code=400)
                    # Check if the user already has the admin role
                    if result["role"] == "admin":
                        return JSONResponse(content={"message": "User is already an admin"}, status_code=200)

                    result1 = signup.update_one({"user": user["user"]}, {"$set": {"role": "admin"}})
                    if result1.modified_count > 0:
                        return JSONResponse(content={"message": "Role updated successfully"}, status_code=200)
                    else:
                        return JSONResponse(content={"message": "User not found"}, status_code=404)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    






