from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import *
from database.database import *
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

# Create an instance of APIRouter to define routes for this specific API section
route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")

# OAuth2 Password Bearer token URL
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
    return html.TemplateResponse("NewShipment.html", {"request": request})

@route.post("/myshipments")
def sign1(request: Request, shipment1: ShipmentData, token: str = Depends(oauth2_scheme)):
    try:
        # Check if any field is empty
        if any(value == "" for value in shipment1.dict().values()):
            raise HTTPException(status_code=400, detail="All fields must be filled")

        # Check if shipment_number has exactly 7 characters
        if len(shipment1.shipment_number) != 7:
            raise HTTPException(status_code=400, detail="Shipment number must be 7 characters")

        existing_data = shipment.find_one({"shipment_number": shipment1.shipment_number}, {"_id": 0})
        if existing_data:
            raise HTTPException(status_code=400, detail="Shipment number already used")

        # Decode token to get user email
        decoded_token = decode_token(token[7:len(token)])

        base = {
            "email": decoded_token["email"],
            'shipment_number': shipment1.shipment_number,
            "container_number": shipment1.container_number,
            "route_details": shipment1.route_details,
            "goods_type": shipment1.goods_type,
            "device": shipment1.device,
            "expected_delivery": shipment1.expected_delivery,
            "po_number": shipment1.po_number,
            "delivery_number": shipment1.delivery_number,
            "ndc_number": shipment1.ndc_number,
            "batch_id": shipment1.batch_id,
            "serial_number": shipment1.serial_number,
            "shipment_description": shipment1.shipment_description
        }

        # Insert shipment data into the database
        shipment.insert_one(base)
        return JSONResponse(content={"error_message": "Shipment Created Successfully"},status_code=200)

    except HTTPException as http_error:
        return JSONResponse(content={"error_message": http_error.detail})












