# from fastapi import APIRouter,Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter,Request,Depends,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import get_current_user
from database.database import *

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")


# @route.get("/shipmenttable")
# def sign(request: Request):
#     return html.TemplateResponse("shipmenttable.html", {"request": request})

# @route.get("/shipmenttable")
# def sign(request: Request):
#     # try:
#     #     if current_user is None:
#             # raise HTTPException(status_code=401, detail="Not authenticated")
#         return html.TemplateResponse("shipmenttable.html", {"request": request})
#     # except Exception as e:
#     #     raise HTTPException(
#     #         status_code=500, detail=f"Internal Server Error: {str(e)}")
@route.get("/shipmenttable")
def sign(request: Request):
    data = test.find({})
    print(data)
    return html.TemplateResponse("shipmenttable.html", {"request": request,"data":data})