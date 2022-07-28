from hashlib import new
import pandas as pd
import numpy as np
import pickle
import joblib

from sklearn.preprocessing import StandardScaler

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


# test_df = pd.read_csv("test.csv")

# loaded_model = pickle.load(open("models\model.pkl", 'rb'))

# prediction=loaded_model.predict(test_df)


def editFrame(df):
    df = df.drop(columns=drop_values, axis=1)
    df = df[df.tenure != 0]
    df["TotalCharges"] = df["TotalCharges"].astype(float)
    df[numerical_values] = scaler.transform(df[numerical_values])
    return df


# def columnCreate(df_test, df_train):
#    df_train = df_train.drop(columns=drop_values, axis=1)
#    df_train = pd.get_dummies(df_train, columns=categorical_values)
#    df_test = df_test.drop(columns=drop_values, axis=1)
#   df_test = df_test.drop(columns="customerID", axis=1)
#   df_test = pd.get_dummies(df_test, columns=categorical_values)
#
#   missing_cols = set(df_train.columns) - set(df_test.columns)
#   for c in missing_cols:
#       df_test[c] = 0
#   df_test = df_test[df_train.columns]
#
#   return df_test


scaler = joblib.load("data/standard_scaler_new.joblib")


def preprocessor(df):
    df = editFrame(df)
    return df[column_order]


# Get missing columns in the training test
# missing_cols = set( train.columns ) - set( test.columns )
# Add a missing column in test set with default value equal to 0
# for c in missing_cols:
#    test[c] = 0
# Ensure the order of column in the test set is in the same order than in train set
# test = test[train.columns]

