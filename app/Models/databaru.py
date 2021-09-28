from mongoengine import Document, StringField, IntField, FloatField, connect

class Databaru(Document):
    battery_power = IntField(required=True)
    blue = IntField(required=True)
    clock_speed = FloatField(required=True)
    dual_sim = IntField(required=True)
    fc = IntField(required=True)
    four_g = IntField(required=True)
    int_memory = IntField(required=True)
    m_dep = FloatField(required=True)
    mobile_wt = IntField(required=True)
    n_cores = IntField(required=True)
    pc = IntField(required=True)
    px_height = IntField(required=True)
    px_width = IntField(required=True)
    ram = IntField(required=True)
    sc_h = IntField(required=True)
    sc_w = IntField(required=True)
    talk_time = IntField(required=True)
    three_g = IntField(required=True)
    touch_screen = IntField(required=True)
    wifi = IntField(required=True)
    price_range = StringField(required=True, max_length=10)

class Database:
    # method yang digunakan untuk koneksi database
    def __init__(self):
        try:
            self.connection = connect(
                db = "mobile_prediction",
                host = "localhost",
                port = 27017
            )
        except Exception as e:
            print(f"kesalahan koneksi database: {e}")

    # method yang digunakan untuk insert databaru ke database
    def insertDataBaru(self, **params):
        try:
            Databaru(**params).save()
        except Exception as e:
            print(f"kesalahan method insertDataBaru: {e}")

    # method yang digunakan untuk melihat semua databaru
    def showAllDataBaru(self):
        try:
            return Databaru.objects().all().to_json()
        except Exception as e:
            print(f"kesalahan method showAllDataBaru: {e}")
