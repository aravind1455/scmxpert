from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
from config.config import signup
from routes.Jwt_Token import create_access_token

route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@route.get("/login")
def login(request: Request):
    return html.TemplateResponse("Login.html", {"request": request})


@route.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    try:
        user_data = signup.find_one({"user": username})
        if user_data:
            if pwd_cxt.verify(password, user_data["password"]):
                token = create_access_token(data={"sub": user_data["user"], "email": user_data["email"], "role": user_data["role"]})
                response_content = {"access_token": token, "username": user_data["user"], "email": user_data["email"], "role": user_data["role"]}
                return JSONResponse(content=response_content, status_code=200)
            else:
                raise HTTPException(status_code=401, detail="Password is incorrect")
        else:
            raise HTTPException(status_code=401, detail="Username not found")
    except HTTPException as http_exception:
        # Handle HTTPException (validation errors) separately
        return JSONResponse(content={"detail": http_exception.detail}, status_code=http_exception.status_code)
    except Exception as e:
        # Handle other exceptions with a 500 status code
        return JSONResponse(content={"detail": str(e)}, status_code=500)










