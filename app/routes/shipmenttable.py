
from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import *
from database.database import *
# from fastapi.security import OAuth2PasswordBearer



route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")


@route.get("/shipmenttable")
def shipment_html(request: Request):
    return html.TemplateResponse("MyShipment.html", {"request": request})

@route.get("/shipment")
def shipment1(request: Request, token: str = Depends(get_current_user)):
    try:
        # print(token)
        # a=decode_token(token)
        # print(a)
        if token:
            # print("token in shipment", a)
            ship_data = list(shipment.find({"email" : token["email"]},{"_id":0}))
            if ship_data:
            # return JSONResponse(content=ship_data, status_code=200)
                return JSONResponse(content=ship_data,status_code=200)
        return HTTPException(status_code=400, detail="Shipments Not Found")
            # return JSONResponse(content={"message": "Token is None"}, status_code=401)
    except HTTPException as http_error:
            return JSONResponse(content={"error_message": http_error.detail})




