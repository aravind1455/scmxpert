from fastapi import APIRouter, HTTPException,Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.Jwt_Token import get_current_user
from database.database import signup 
from fastapi.responses import JSONResponse 


route=APIRouter()

html = Jinja2Templates(directory = "Templates")

route.mount("/project", StaticFiles(directory="project"), name = "project")

@route.get("/changerole")
def email(request: Request):
    return html.TemplateResponse("UpdateRole.html", {"request": request})

    
@route.post("/changeroleuser")
def change(request: Request, user: dict, token: str = Depends(get_current_user)):
    try:
        if not token:
            return JSONResponse(content={"message": "Unauthorized"}, status_code=401)
        
        if not user or not user.get("user"):
            return JSONResponse(content={"message": "Please provide a valid user"}, status_code=400)
        
        result = signup.find_one({"user": user["user"]})
        
        if not result:
            return JSONResponse(content={"message": "User not found"}, status_code=404)
        
        if token["role"] == "user":
            return JSONResponse(content={"message": "You are not authorized to change roles"}, status_code=403)
        
        # Check if the user already has the admin role
        if result["role"] == "admin":
            return JSONResponse(content={"message": "User is already an admin"}, status_code=200)

        result1 = signup.update_one({"user": user["user"]}, {"$set": {"role": "admin"}})
        if result1.modified_count > 0:
            return JSONResponse(content={"message": "Role updated successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Role update failed"}, status_code=500)

    except Exception:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)






