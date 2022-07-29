from main import make_prediction
from data.data import editFrame, preprocessor
import pandas as pd
import unittest


example_json = {
    "customerID": 1,
    "tenure": 200,
    "MonthlyCharges": 53.85,
    "TotalCharges": 108.15,
    "SeniorCitizen": 0,
    "gender": 1,
    "Partner": 0,
    "Dependents": 0,
    "PhoneService": 1,
    "MultipleLines": 0,
    "InternetService": 1,
    "OnlineSecurity": 1,
    "OnlineBackup": 1,
    "DeviceProtection": 0,
    "TechSupport": 0,
    "StreamingTV": 0,
    "StreamingMovies": 0,
    "Contract": 0,
    "PaperlessBilling": 1,
    "PaymentMethod": 1,
}

record = [
    {
        "customerID": 1,
        "tenure": 200,
        "MonthlyCharges": 53.85,
        "TotalCharges": 108.15,
        "SeniorCitizen": 0,
        "gender": 1,
        "Partner": 0,
        "Dependents": 0,
        "PhoneService": 1,
        "MultipleLines": 0,
        "InternetService": 1,
        "OnlineSecurity": 1,
        "OnlineBackup": 1,
        "DeviceProtection": 0,
        "TechSupport": 0,
        "StreamingTV": 0,
        "StreamingMovies": 0,
        "Contract": 0,
        "PaperlessBilling": 1,
        "PaymentMethod": 1,
    }
]


class test_prediction(unittest.TestCase):
    def test_prediction(self):
        self.assertTrue(bool(make_prediction(example_json)))

    def test_editFrame(self):
        self.assertFalse(bool(editFrame(pd.DataFrame.from_records(record)).empty))

    def test_preprocessor(self):
        self.assertFalse(bool(preprocessor(pd.DataFrame.from_records(record)).empty))


if __name__ == "__main__":
    unittest.main()

