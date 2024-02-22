from pydantic import BaseModel

class Signup(BaseModel):
    user: str
    email: str
    role: str
    password: str
    confirmpassword: str

# Define a Pydantic model for representing shipment data in the request body
class ShipmentData(BaseModel):
    shipment_number: int
    container_number: int
    route_details: str
    goods_type: str
    device: int
    expected_delivery: str
    po_number: int
    delivery_number: int
    ndc_number: int
    batch_id: int
    serial_number: int
    shipment_description: str

class DeviceData(BaseModel):
    Battery_Level: float
    Device_Id: int
    First_Sensor_temperature: float
    Route_From: str
    Route_To: str