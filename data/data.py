import pandas as pd
import numpy as np



from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,roc_curve,classification_report
from sklearn.model_selection import GridSearchCV


from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
from sklearn.utils import compute_class_weight


numerical_values=["tenure","MonthlyCharges","log_totalcharges"]

drop_values=["gender","PhoneService","MultipleLines","TotalCharges"]

categorical_values=[ 'SeniorCitizen', 'Partner', 'Dependents',
             'InternetService','OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
           'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
           'PaymentMethod']
           

test_df = pd.read_csv(test.csv)



def preprocessor(df):

  return processed_df