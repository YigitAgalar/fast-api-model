import pandas as pd
import numpy as np
import joblib


numerical_values = ["tenure", "MonthlyCharges", "TotalCharges"]

drop_values = ["customerID", "gender", "PhoneService", "MultipleLines"]

categorical_values = [
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
]

column_order = [
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges",
]



def editFrame(df):
    df = df.drop(columns=drop_values, axis=1)
    df = df[df.tenure != 0]
    df["TotalCharges"] = df["TotalCharges"].astype(float)
    df[numerical_values] = scaler.transform(df[numerical_values])
    return df



scaler = joblib.load("data/standard_scaler_new.joblib")


def preprocessor(df):
    df = editFrame(df)
    return df[column_order]

