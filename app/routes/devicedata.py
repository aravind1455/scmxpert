# from fastapi import APIRouter, HTTPException,Request,Depends
# from fastapi.responses import JSONResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from pymongo import MongoClient
# from routes.login import *
# from routes.login import get_current_user
# from fastapi import Request, Depends, Form, HTTPException, status, Response


# client = MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
# db = client['aravind']  # Replace with your MongoDB database name
# collection = db['DeviceData']  

# route=APIRouter()
# html = Jinja2Templates(directory = "Templates")
# route.mount("/project", StaticFiles(directory="project"), name = "project")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     payload = decode_token(token)
#     # print(token)
#     if payload and "sub" in payload and "email" in payload:
#         user_data = signup.find_one({"email": payload["email"]})
#         # print(user_data)
#         if user_data :
#             return user_data

# # Route to display the device data
# @route.get("/devicedata")
# def sign(request: Request):
#         # ship_data = list(collection.find({""}, {'_id': 0}))
#         return html.TemplateResponse("devicedata.html", {"request": request})
 
    
# from fastapi.responses import JSONResponse

# @route.post("/devicedatafirst")
# async def get_device_data(request: Request,token : str = Depends(oauth2_scheme)):
#     try:
#         if token:
#             data1 = await request.json()
#             device_id = data1.get("Device_ID")
#             # print(device_id)
#             if device_id:
#                 # Assuming you want to filter data based on the received device_id {"Device_ID": device_id}
#                 ship_data = list(collection.find({'Device_ID': int(device_id)}, {'_id': 0}))
#                 # print(ship_data)
#                 return JSONResponse(content={"data": ship_data}, status_code=200)
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)

from fastapi import APIRouter, Request, Depends, HTTPException, status, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from routes.login import decode_token, signup, OAuth2PasswordBearer, get_current_user

client = MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
db = client['aravind']  # Replace with your MongoDB database name
collection = db['DeviceData']

route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if payload and "sub" in payload and "email" in payload:
        user_data = signup.find_one({"email": payload["email"]})
        if user_data:
            return user_data

# Route to display the device data
@route.get("/devicedata")
def sign(request: Request):
    return html.TemplateResponse("devicedata.html", {"request": request})

# Route to get device data based on Device_ID
@route.post("/devicedatafirst")
async def get_device_data(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        if token:
            data1 = await request.json()
            device_id = data1.get("Device_ID")
            if device_id:
                # Assuming you want to filter data based on the received device_id {"Device_ID": device_id}
                ship_data = list(collection.find({'Device_ID': int(device_id)}, {'_id': 0}))
                return JSONResponse(content={"data": ship_data}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)





