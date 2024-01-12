from fastapi import APIRouter, HTTPException,Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import get_current_user
from fastapi import Request, Depends, Form, HTTPException, status, Response

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")

# Route to display the device data
@route.get("/devicedata")
def sign(request: Request):
        return html.TemplateResponse("devicedata.html", {"request": request})
 

@route.post("/devicedata")
async def updaterole(request: Request,current_user: dict = Depends(get_current_user)):
        if current_user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    