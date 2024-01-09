from fastapi import APIRouter, HTTPException,Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import get_current_user

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")


# @route.get("/devicedata")
# def sign(request: Request):
#     return html.TemplateResponse("devicedata.html", {"request": request})
# #     try:
# #         if current_user is None:
# #             raise HTTPException(status_code=401, detail="Not authenticated")

#     # except Exception as e:
#     #     raise HTTPException(
#     #         status_code=500, detail=f"Internal Server Error: {str(e)}")
@route.get("/devicedata")
def sign(request: Request,current_user: dict = Depends(get_current_user)):
    try:
        if current_user is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        return html.TemplateResponse("devicedata.html", {"request": request})
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}")
    