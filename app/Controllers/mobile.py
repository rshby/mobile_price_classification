import pandas as pd 
import numpy as np 
import pickle
import json
from Models.databaru import Database

db = Database()

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
        
        dataToInsert = {
            "battery_power": int(params["battery_power"]),
            "blue": int(params["blue"]),
            "clock_speed": float(params["clock_speed"]),
            "dual_sim": int(params["dual_sim"]),
            "fc": int(params["fc"]),
            "four_g": int(params["four_g"]),
            "int_memory": int(params["int_memory"]),
            "m_dep": float(params["m_dep"]),
            "mobile_wt": int(params["mobile_wt"]),
            "n_cores": int(params["n_cores"]),
            "pc": int(params["pc"]),
            "px_height": int(params["px_height"]),
            "px_width": int(params["px_width"]),
            "ram": int(params["ram"]),
            "sc_h": int(params["sc_h"]),
            "sc_w": int(params["sc_w"]),
            "talk_time": int(params["talk_time"]),
            "three_g": int(params["three_g"]),
            "touch_screen": int(params["touch_screen"]),
            "wifi": int(params["wifi"]),
            "price_range" : str(hasilPrediksi[0])
        }
        db.insertDataBaru(**dataToInsert)
        return str(hasilPrediksi[0])
    except Exception as e:
        print(f"kesalahan function showPrediction: {e}")

# function yang digunakan untuk convert ObjectId ke string
def ObjToStr(obj):
    try:
        return str(obj["_id"]["$oid"])
    except Exception as e:
        print(f"kesalahan fucntion ObjToStr: {e}")

# function yang digunakan untuk melihat databaru dari database
def showAllDataBaru():
    try:
        dbhasil = db.showAllDataBaru()
        hasil = json.loads(dbhasil)
        data_list = []
        for data in hasil:
            data["id"] = ObjToStr(data)
            data_list.append(data)
        return data_list
    except Exception as e:
        print(f"kesalahan function showAllDatabaru: {e}")

# function yang digunakan untuk melihat data hasil_prediksi
def showHasilPrediksi():
    try:
        return pd.read_feather(r"C:\Users\ROG\Documents\mobile_price_classification\experiment\hasil_prediksi.feather").to_dict(orient="records")
    except Exception as e:
        print(f"kesalahan function showHasilPrediksi: {e}")