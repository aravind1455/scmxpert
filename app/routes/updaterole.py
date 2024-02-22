from fastapi import APIRouter, HTTPException,Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.Jwt_Token import get_current_user
from config.config import signup 
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
        # Ensure authentication token is present
        if not token:
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Ensure user data is provided and valid
        if not user or not user.get("user"):
            raise HTTPException(status_code=400, detail="Please provide a valid user")

        # Query user data from the database
        result = signup.find_one({"user": user["user"]})
        if not result:
            raise HTTPException(status_code=404, detail="User not found")

        # Check authorization
        if token["role"] == "user":
            raise HTTPException(status_code=403, detail="You are not authorized to change roles")

        # Check if the user already has the admin role
        if result["role"] == "admin":
            return JSONResponse(content={"message": "User is already an admin"}, status_code=400)

        # Update user role to admin
        result1 = signup.update_one({"user": user["user"]}, {"$set": {"role": "admin"}})
        if result1.modified_count > 0:
            return JSONResponse(content={"message": "Role updated successfully"}, status_code=200)
        else:
            raise HTTPException(status_code=500, detail="Role update failed")

    except HTTPException as http_error:
        return JSONResponse(content={"message": http_error.detail}, status_code=http_error.status_code)

    except Exception as e:
        return JSONResponse(content={"message": "Internal server error", "error": str(e)}, status_code=500)







