# Import necessary modules and classes from FastAPI
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Import route instances from separate route files
from routes.dashboard import route as dash
from routes.myshipments import route as ship
from routes.shipmenttable import route as shiptable
from routes.devicedata import route as device
from routes.login import route as log
from routes.signup import route as sign
from routes.myaccount import route as account
from routes.starting import route as start
from routes.email import route as email

# Create a FastAPI instance
app = FastAPI()

# Specify allowed origins for CORS (Cross-Origin Resource Sharing)
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

# Configure CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an instance of Jinja2Templates to handle rendering HTML templates
html = Jinja2Templates(directory="HTML")

# Mount the "project" directory containing static files (e.g., CSS, JS) under the "/project" route
app.mount("/project", StaticFiles(directory="project"), name="project")

# Include routers for each route file
app.include_router(dash)
app.include_router(ship)
app.include_router(shiptable)
app.include_router(device)
app.include_router(log)
app.include_router(sign)
app.include_router(account)
app.include_router(start)
app.include_router(email)

