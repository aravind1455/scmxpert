import secrets
import pymongo
dburl="mongodb+srv://aravindsvec123:4bwm2d4mPsrAubxJ@cluster0.zef7rbt.mongodb.net/"
connection=pymongo.MongoClient(dburl)

projectdb=connection["SCMXpert"]
shipment=projectdb["ShipmentData"]
signup=projectdb["signup"]


SECRET_KEY=secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30





