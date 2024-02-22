from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import shipment
from routes.Jwt_Token import oauth2_scheme,decode_token
from models.models import ShipmentData

# Create an instance of APIRouter to define routes for this specific API section
route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")



@route.get("/Newshipments")
def sign(request: Request):
    return html.TemplateResponse("NewShipment.html", {"request": request})

@route.post("/Newshipments")
def sign1(request: Request, shipment1: ShipmentData, token: str = Depends(oauth2_scheme)):
    try:
        # Check if any field is empty
        if any(value == "" for value in shipment1.dict().values()):
            raise HTTPException(status_code=400, detail="All fields must be filled")

        # Check if shipment_number has exactly 7 characters
        if len(str(shipment1.shipment_number)) != 7:
            raise HTTPException(status_code=400, detail="Shipment number must be 7 characters")

        existing_data = shipment.find_one({"shipment_number": shipment1.shipment_number}, {"_id": 0})
        if existing_data:
            raise HTTPException(status_code=400, detail="Shipment number already used")

        # Decode token to get user email
        decoded_token = decode_token(token[7:len(token)])
        # print(decoded_token)

        base = {
            "user":decoded_token["sub"],
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
    except Exception as e:
        # Handle other exceptions with a 500 status code
        return JSONResponse(content={"detail": str(e)}, status_code=500)












