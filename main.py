from multiprocessing.sharedctypes import Value
from fastapi import FastAPI
from pydantic import BaseModel, root_validator,validator
import pandas as pd

app= FastAPI()



class Data(BaseModel):
    tenure:int
    MonthlyCharges:float
    TotalCharges:float
    SeniorCitizen:int
    gender:str
    Partner:str
    Dependents:str
    PhoneService:str         
    MultipleLines:str        
    InternetService:str      
    OnlineSecurity:str       
    OnlineBackup:str         
    DeviceProtection:str     
    TechSupport:str         
    StreamingTV:str        
    StreamingMovies: str     
    Contract:str             
    PaperlessBilling:str     
    PaymentMethod:str        


    @root_validator()
    def validate_all(cls,values):
        if values["SeniorCitizen"] == "" or " " in values["SeniorCitizen"] :
            raise ValueError("SeniorCitizen can't be null")
        if values["Partner"] =="":
            raise ValueError("Partner can't be null")


  #'Partner', 'Dependents',
   #          'InternetService','OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
    #       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
     #      'PaymentMethod']
   
    @validator("MonthlyCharges")
    def validate_tenure(cls,value):
        if value <= 0:
            raise ValueError("MonthlyCharges >0 olmalı")
        return value
    


@app.get("/")
def root():
    return {"message":"alive"}




@app.post("/predict")
def make_prediction(data:Data):
    

    return  data