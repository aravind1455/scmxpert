
# from fastapi import APIRouter, Request, Form
# from fastapi.responses import JSONResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from database.database import signup  # Assuming signup is the MongoDB collection
# from datetime import datetime, timedelta
# from jose import jwt
# from fastapi.security import OAuth2PasswordBearer
# from typing import Optional 



# route = APIRouter()
# html = Jinja2Templates(directory="Templates")
# route.mount("/project", StaticFiles(directory="project"), name="project")

# @route.get("/login")
# def login(request: Request):
#     return html.TemplateResponse("login.html", {"request": request})

# @route.post("/login")
# def login(request: Request, username: str = Form(...)):
#     var = signup.find_one({"user": username})

#     if var:
#         token = create_access_token(data={"sub": var["user"],
#                                           "email":var["email"],
#                                           "role":var["role"]
#                                           })
#         response_content = {
#             "access_token": token,
#             "username": var["user"],
#             "email":var["email"],
#                 "role":var["role"]
#         }
#         return JSONResponse(content=response_content, status_code=200)
#     else:
#         response_content = {"detail": "Invalid credentials"}
#         return JSONResponse(content=response_content, status_code=401)



# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# from passlib.context import CryptContext
# from jose import jwt, ExpiredSignatureError, JWTError
# from fastapi.security import OAuth2PasswordBearer
# from fastapi import Depends, HTTPException, status, Request, Cookie
# from datetime import datetime, timedelta
# from typing import Optional, Union
# import os
# # from dotenv import load_dotenv
# from database.database import *
# import secrets



# # Create an instance of CryptContext for password hashing and verification
# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # class Hash:
# #     def hash_password(pwd: str):   #hashing the password
# #         return pwd_cxt.hash(pwd)

# #     def verify_password(pwd: str, hashed_password: str):  #verify the hashed password
# #         return pwd_cxt.verify(pwd, hashed_password)

# # Load environment variables for JWT configuration



# # OAuth2PasswordBearer for token authentication
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ###### ----------function to create access token(JWT) for user authenication----------######

# def create_access_token(data: dict, expires_delta:Optional[timedelta] = None):
#     to_encode = data.copy()   # Make a copy of the input data dictionary
#     # Calculate the token expiration time
#     if expires_delta: 
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt



# ###### ----------function decode the JWT token----------######

# def decode_token(token: str):
#     try:
#         # Attempt to decode the provided token
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except ExpiredSignatureError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})



# ###### ----------function to get current user from access token----------######

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = decode_token(token)
#         if payload and "sub" in payload and "email" in payload:
#             user_data = signup.find_one({"email": payload["email"]})
#             if user_data and "username" in user_data:
#                 return user_data
#     except JWTError:
#         pass

#     return None



 
 
# # #authenticating user
# # async def authenticate_user(email: str, password: str):
# #     loop = asyncio.get_event_loop()
# #     user = await loop.run_in_executor(None, lambda: signup.find_one({"email": email}))
# #     if not user or not Hashpass.verify_password(password, user['password']):
# #         return False
# #     return user
 
 
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


@route.post("/login")
def login(request: Request, username: str = Form(...),password:str = Form(...)):
    # user_data = signup.find_one({"user": username})
    query = {
        "$and": [
            {"user": username},
            {"password": password}
        ]
    }
    # Find one document that matches both username and password conditions
    user_data = signup.find_one(query)

    if user_data:
        token = create_access_token(data={
            "sub": user_data["user"],
            "email": user_data["email"],
            "role": user_data["role"]
        })
        response_content = {
            "access_token": token,
            "username": user_data["user"],
            "email": user_data["email"],
            "role": user_data["role"]
        }
        return JSONResponse(content=response_content, status_code=200)
    else:
        response_content = {"detail": "Invalid credentials"}
        return JSONResponse(content=response_content, status_code=401)


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
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired",
                            headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token",
                            headers={"WWW-Authenticate": "Bearer"})


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        if payload and "sub" in payload and "email" in payload:
            user_data = signup.find_one({"email": payload["email"]})
            if user_data and "username" in user_data:
                return user_data
    except JWTError:
        pass

    return None
