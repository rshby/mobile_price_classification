import pandas as pd 
import numpy as np 
import pickle

model = pickle.load(open(r"C:\Users\ROG\Documents\mobile_price_classification\experiment\model_xgb.pkl", 'rb'))

# function yang digunakan untuk melihat semua data training
def showDataTrain():
    try:
        df = pd.read_csv(r"C:\Users\ROG\Documents\mobile_price_classification\dataset\train.csv")
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"{e}")
