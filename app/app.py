from fastapi import FastAPI
from starlette.middleware.cors import ALL_METHODS
from starlette.routing import Host
from Controllers import mobile
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# route API untuk get semua data train
@app.get("/train")
async def dataTrain():
    try:
        hasil = mobile.showDataTrain()
        data = {
            "message": "success",
            "data": hasil
        }
        return data
    except Exception as e:
        print(f"kesalahan API dataTrain: {e}")

# route API yang digunakan untuk memprediksi data
@app.get("/prediksi")
async def prediksiData(params: dict):
    try:
        hasil = mobile.showPrediction(**params)
        data = {
            "message": "success",
            "prediksi": hasil
        }
        return data
    except Exception as e:
        print(f"kesalahan API prediksiData : {e}")


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8008, reload=True)