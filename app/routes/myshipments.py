from fastapi import APIRouter,Request,Depends,HTTPException,Form, Header
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import decode_token, get_current_user
from database.database import *

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")



    


from fastapi import APIRouter, Request, Form,status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import *
from pydantic import BaseModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Define a Pydantic model for representing shipment data in the request body
class ShipmentData(BaseModel):
    shipment_number: str
    container_number: str
    route_details: str
    goods_type: str
    device: str
    expected_delivery: str
    po_number: str
    delivery_number: str
    ndc_number: str
    batch_id: str
    serial_number: str
    shipment_description: str




@route.get("/myshipments")
def sign(request: Request):
        return html.TemplateResponse("myshipments.html", {"request": request})
   
    
@route.post("/myshipments")
def sign1(request: Request, shipment1: ShipmentData , token : str = Depends(oauth2_scheme)): 
    print(token[7:len(token)])
    a=decode_token(token[7:len(token)])
    print(a)

    base={
         "email":a["email"],
        'shipment_number':shipment1.shipment_number,
        "container_number":shipment1.container_number,
        "route_details":shipment1.route_details,
        "goods_type":shipment1.goods_type, 
        "device":shipment1.device,
        "expected_delivery":shipment1.expected_delivery,
        "po_number":shipment1.po_number,
        "delivery_number":shipment1.delivery_number,
        "ndc_number":shipment1.ndc_number,
        "batch_id":shipment1.batch_id,
        "serial_number":shipment1.serial_number,
        "shipment_description":shipment1.shipment_description
    }
    shipment.insert_one(base)
    return {"message": "Shipment Created Successfully"}
    # try:
    #     # Check if the shipment is already registered
    #     existing_shipment = shipment.find_one({"shipment_number": shipment1.shipment_number})

    #     if existing_shipment:
    #         raise HTTPException(status_code=400, detail="Shipment already exists")
    # # print(token, request, shipment1)
        
    # except HTTPException as http_error:
    #     if http_error.detail == "Shipment already exists":
    #         raise HTTPException(status_code=400, detail=http_error.detail)
    #     raise http_error  
    
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")



   


