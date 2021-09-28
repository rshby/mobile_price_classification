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
        print(f"kesalahan function showDataTrain: {e}")

# function yang digunakan untuk memprediksi Data
def showPrediction(**params):
    try:
        data = [[
            int(params["battery_power"]),
            int(params["blue"]),
            float(params["clock_speed"]),
            int(params["dual_sim"]),
            int(params["fc"]),
            int(params["four_g"]),
            int(params["int_memory"]),
            float(params["m_dep"]),
            int(params["mobile_wt"]),
            int(params["n_cores"]),
            int(params["pc"]),
            int(params["px_height"]),
            int(params["px_width"]),
            int(params["ram"]),
            int(params["sc_h"]),
            int(params["sc_w"]),
            int(params["talk_time"]),
            int(params["three_g"]),
            int(params["touch_screen"]),
            int(params["wifi"])
        ]]
        data_test = pd.DataFrame(data, index=[0], columns=['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g','touch_screen', 'wifi'])
        hasilPrediksi = model.predict(data_test)
        return str(hasilPrediksi[0])
    except Exception as e:
        print(f"kesalahan function showPrediction: {e}")
