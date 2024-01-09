from fastapi import APIRouter,Request,Depends,HTTPException,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import get_current_user
from database.database import *

route=APIRouter()
html = Jinja2Templates(directory = "Templates")
route.mount("/project", StaticFiles(directory="project"), name = "project")



    


from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import *
from pydantic import BaseModel

route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")

# class ShipmentData(BaseModel):
#     shipment_number: str
#     container_number: str
#     route_details: str
#     goods_type: str
#     device: str
#     expected_delivery: str
#     po_number: str
#     delivery_number: str
#     ndc_number: str
#     batch_id: str
#     serial_number: str
#     shipment_description: str


# @route.post("/myshipments")
# def post_shipment(request: Request, shipment_data: ShipmentData):
#     base = shipment_data.dict()
#     shipment.insert_one(base)
#     return html.TemplateResponse("myshipments.html", {"request": request})

@route.get("/myshipments")
def sign(request: Request):
        return html.TemplateResponse("myshipments.html", {"request": request})
   
    

@route.post("/myshipments")
def sign1(request: Request,shipment_number:str = Form(...),container_number:str = Form(...),route_details:str = Form(...),goods_type:str = Form(...),device:str = Form(...),expected_delivery:str = Form(...),po_number:str = Form(...),delivery_number:str = Form(...),ndc_number:str = Form(...),batch_id:str = Form(...),serial_number:str = Form(...),shipment_description:str = Form(...)):
    base={
        'shipment number':shipment_number,
        "container number":container_number,
        "route details":route_details,
        "goods type":goods_type,
        "device":device,
        "expected_delivery":expected_delivery,
        "po number":po_number,
        "delivery number":delivery_number,
        "ndc number":ndc_number,
        "batch id":batch_id,
        "serial number":serial_number,
        "shipment description":shipment_description
    }
    shipment.insert_one(base)
    return html.TemplateResponse("myshipments.html", {"request": request})