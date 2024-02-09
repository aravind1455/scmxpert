from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.Jwt_Token import get_current_user
from database.database import shipment



route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")


@route.get("/shipmenttable")
def shipment_html(request: Request):
    return html.TemplateResponse("MyShipment.html", {"request": request})

@route.get("/shipment")
def shipment1(request: Request, token: str = Depends(get_current_user)):
    try:
        if token:
            ship_data = list(shipment.find({"email" : token["email"]},{"_id":0}))
            if ship_data:
                return JSONResponse(content=ship_data,status_code=200)
        return HTTPException(status_code=400, detail="Shipments Not Found")
    
    except HTTPException as http_error:
            return JSONResponse(content={"error_message": http_error.detail})




