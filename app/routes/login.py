from fastapi import APIRouter, Request, Form, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
from jose import jwt, ExpiredSignatureError, JWTError
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from typing import Optional
from database.database import signup  # Assuming signup is the MongoDB collection

route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")

# OAuth2PasswordBearer for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Create an instance of CryptContext for password hashing and verification
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


@route.get("/login")
def login(request: Request):
    return html.TemplateResponse("login.html", {"request": request})



from fastapi import HTTPException

from fastapi import HTTPException
from fastapi import HTTPException, Request, Form
from fastapi.responses import JSONResponse

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


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Check token expiration
        if payload["exp"] <= datetime.utcnow().timestamp():
            raise ExpiredSignatureError("Token has expired")
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired",
                            headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token",
                            headers={"WWW-Authenticate": "Bearer"})

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # print(token)
        payload = decode_token(token)
        if payload and "sub" in payload and "email" in payload:
            # print(payload,"payload")
            user_data = signup.find_one({"email": payload["email"]})
            # print(user_data,"user")
            if user_data :
                # print(user_data)
                return user_data
    except JWTError:
        pass

    return None
