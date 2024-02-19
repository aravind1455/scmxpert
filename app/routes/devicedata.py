from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from routes.Jwt_Token import get_current_user

client = MongoClient('mongodb+srv://aravindsvec123:4bwm2d4mPsrAubxJ@cluster0.zef7rbt.mongodb.net/')  
db = client['SCMXpert'] 
collection = db['DeviceData']


route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")


@route.get("/devicedata")
def sign(request: Request):
    return html.TemplateResponse("DeviceData.html", {"request": request})

# Route to get device data based on Device_ID
@route.post("/devicedatafirst")
async def get_device_data(request: Request, token: str = Depends(get_current_user)):
    try:
        if token:
            data1 = await request.json()
            # print(type(data1))
            device_id = data1.get("Device_ID")
            # print(type(device_id))
            if device_id:
                # Assuming you want to filter data based on the received device_id {"Device_ID": device_id}
                ship_data = list(collection.find({'Device_ID': int(device_id)}, {'_id': 0}))
                if ship_data:
                    return JSONResponse(content={"data": ship_data}, status_code=200)
            return HTTPException(status_code=400, detail="Device Data Not Found")
    except HTTPException as http_error:
            return JSONResponse(content={"error_message": http_error.detail})
    except Exception as e:
        # Handle other exceptions with a 500 status code
        return JSONResponse(content={"detail": str(e)}, status_code=500)





