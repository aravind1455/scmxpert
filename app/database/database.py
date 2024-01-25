import pymongo
dburl="mongodb+srv://aravindsvec123:4bwm2d4mPsrAubxJ@cluster0.zef7rbt.mongodb.net/"
connection=pymongo.MongoClient(dburl)

projectdb=connection["SCMXpert"]
test=projectdb["test"]
shipment=projectdb["ShipmentData"]
signup=projectdb["signup"]




# class UserCreate(BaseModel):
#     username: str 
#     email: EmailStr 
#     password: str
#     confirm_password: str
#     role: str = Field(default="User") 

