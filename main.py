from multiprocessing.sharedctypes import Value
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from sklearn.linear_model import LogisticRegression
from pydantic import BaseModel, root_validator, validator
import pickle
import pandas as pd
from data.data import preprocessor
from logger import logger
import re
import io
from sqlalchemy import create_engine


engine = create_engine(
   )


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


@app.get("/")
def root():
    logger.warning("logging from the root logger")
    return {"message": "alive"}


@app.post("/predict")
def make_prediction(data: Data):
    
    logger.warning("Endpointe veri geldi")
    json_item = jsonable_encoder(data)
    df_new = pd.DataFrame(json_item, index=[0])
    logger.warning("Veri preprocesse girdi")
    df_processed = preprocessor(df_new)
    logger.warning("Model tahmine basladi")
    # a=loaded_model.predict_proba(df_processed)[0]
    a = loaded_model.predict(df_processed)[0]
    logger.warning(
        f" customerID ={df_new.loc[0,'customerID']};  tahmin edilen sonuc ;{a};")
    logger.warning("-"*20)
    query= """INSERT INTO loglar ("timestamp","customerID",churn_prediction) VALUES ({0},{1},{2}) """.format(timestamp,df_new.loc[0,'customerID'],a)
    log_to_df(log_split())
    return {"Churn": f"{a}"}

# LOG OPERATIONS


def log_split():
    data = []
    order = ["timestamp", "customerID", "churn_prediction"]
    indices_to_access = [0, 2, 4]
    file_name = "logdeneme.log"
    file = open(file_name, "r")
    for line in file.readlines():
        if "customerID" in line:
            details = re.split(r'[,|;=!]', line)
            a_series = pd.Series(details)
            accessed_series = a_series[indices_to_access]
            structure = {key: value for key,
                         value in zip(order, accessed_series)}
            data.append(structure)

    return data


def log_to_df(data_dict):
    table = "deneme"
    df = pd.DataFrame.from_records(data_dict)
    df["timestamp"] = pd.to_datetime(df['timestamp'])
    df.to_csv("deneme.csv", sep=",", index=False)
    ddl = pd.io.sql.get_schema(df, table, con=engine)
    print(ddl)
