from multiprocessing.sharedctypes import Value
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from sklearn.linear_model import LogisticRegression
from pydantic import BaseModel, root_validator, validator
import pickle
import pandas as pd
from data.data import preprocessor

app = FastAPI()

loaded_model = pickle.load(open("models\model.pkl", "rb"))


class Data(BaseModel):
    customerID: int
    tenure: float
    MonthlyCharges: float
    TotalCharges: float
    SeniorCitizen: int
    gender: int
    Partner: int
    Dependents: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int

    #'Partner', 'Dependents',
    #          'InternetService','OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
    #       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
    #      'PaymentMethod']

    @validator("MonthlyCharges")
    def validate_tenure(cls, value):
        if value <= 0:
            raise ValueError("MonthlyCharges >0 olmalı")
        return value


@app.get("/")
def root():
    return {"message": "alive"}


@app.post("/predict")
def make_prediction(data: Data):
    json_item = jsonable_encoder(data)
    df_new = pd.DataFrame(json_item, index=[0])
    df_write = preprocessor(df_new)
    a=loaded_model.predict(df_write)[0]
    
    return {"Churn":f"{a}"}

