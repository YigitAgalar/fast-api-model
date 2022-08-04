from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, validator
import pickle
import pandas as pd
from data.data import preprocessor
from logger import logger
import re
import time
from sqlalchemy import create_engine
from fastapi_utils.tasks import repeat_every
from datetime import datetime
from pathlib import Path
from data.db import postgre_insert


engine = create_engine(""
   )
table = "loglar"

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

    @validator("MonthlyCharges")
    def validate_monthly(cls, value):
        if value <= 0:
            raise ValueError("MonthlyCharges >0 olmalı")
        return value

    @validator("tenure")
    def validate_tenure(cls, value):
        if value <= 0:
            raise ValueError("tenure  >0 olmalı")
        return value



@app.on_event("startup")
@repeat_every(wait_first=True,seconds= 1 * 30)  #1 hour 60*60
def write_logs_db() -> None:
    path_to_file = f"logs/{datetime.now().strftime('%d-%m-%Y')}.log"
    path = Path(path_to_file)
    if path.is_file():
        start_time=time.time()
        logger.warning(f"dbye yazma islemi basladi")
        postgre_insert(engine,table,log_split())
        logger.warning(f"dbye yazma islemi bitti, Islem {(time.time()-start_time)*1000} ms surdu")
    else:
        logger.error(f"logs/{datetime.now().strftime('%d-%m-%Y')}.log bulunmuyor dbye yazim islemi yapilmadi")
    



@app.get("/")
def root():
    logger.warning("logging from the root logger")
    return {"message": "alive"}


@app.post("/predict")
def make_prediction(data: Data):
    start_time=time.time()
    logger.warning("Endpointe veri geldi")
    json_item = jsonable_encoder(data)
    df_new = pd.DataFrame(json_item, index=[0])
    logger.warning("Veri preprocesse girdi")
    df_processed = preprocessor(df_new)
    logger.warning("Model tahmine basladi")
    # a=loaded_model.predict_proba(df_processed)[0]
    a = loaded_model.predict(df_processed)[0]
    logger.warning(f"Islem {time.time()-start_time} ms surdu") 
    logger.warning(
        f" customerID ={df_new.loc[0,'customerID']};  tahmin edilen sonuc ;{a};")
       
    logger.warning("----"*20)
    
    return {"Churn": f"{a}"}

# LOG OPERATIONS


def log_split():
    data = []
    order = ["timestamp", "customerID", "churn_prediction"]
    indices_to_access = [0, 2, 4]
    file_name = f"logs/{datetime.now().strftime('%d-%m-%Y')}.log"
    file = open(file_name, "r")
    for line in file.readlines():
        if "customerID" in line:
            details = re.split(r'[,|;=!]', line)
            a_series = pd.Series(details)
            accessed_series = a_series[indices_to_access]
            structure = {key: value for key,
                         value in zip(order, accessed_series)}
            data.append(structure)

    df = pd.DataFrame.from_records(data)
    df["timestamp"] = pd.to_datetime(df['timestamp'])
    return df


    
