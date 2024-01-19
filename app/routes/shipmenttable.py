# from fastapi import APIRouter,Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles




# @route.get("/shipmenttable")
# def sign(request: Request):
#     data = shipment.find({})
#     return html.TemplateResponse("shipmenttable.html", {"request": request,"data":data})


from fastapi import APIRouter, Request, Depends, HTTPException, status,Header
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import *
from database.database import *
from fastapi.security import OAuth2PasswordBearer
import pymongo

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")


# Assuming you have an oauth2_scheme defined like this:
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    # print(token)
    if payload and "sub" in payload and "email" in payload:
        user_data = signup.find_one({"email": payload["email"]})
        # print(user_data)
        if user_data :
            return user_data

@route.get("/shipmenttable")
def shipment_html(request: Request):
    return html.TemplateResponse("shipmenttable.html", {"request": request})

@route.get("/shipment")
def shipment1(request: Request, token: str = Depends(get_current_user)):
    # print(token)
    # a=decode_token(token)
    # print(a)
    if token:
        # print("token in shipment", a)
        ship_data = list(shipment.find({"email" : token["email"]},{"_id":0}))
        return JSONResponse(content=ship_data, status_code=200)
        # return JSONResponse(content={"message": "Token is None"}, status_code=401)




