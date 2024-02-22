from fastapi import Depends, HTTPException, status
from jose import jwt, ExpiredSignatureError, JWTError
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from typing import Optional
from config.config import signup,SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# Function to create an access token with an optional expiration time (expires_delta).

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Function to decode a token, checking for expiration and handling exceptions.
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
    
    
#A function that depends on the oauth2_scheme to extract and validate the access token. 
#It uses the decode_token function to decode the token and fetch user data from the database.
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