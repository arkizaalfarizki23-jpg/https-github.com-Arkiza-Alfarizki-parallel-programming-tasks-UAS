from database import SessionLocal, SensorLog

db = SessionLocal()

data = [
    SensorLog(lokasi="Gudang A", suhu=30.5, kelembapan=70),
    SensorLog(lokasi="Gudang B", suhu=28.0, kelembapan=65),
    SensorLog(lokasi="Gudang C", suhu=31.2, kelembapan=75),
]

db.add_all(data)
db.commit()
db.close()

print("Data berhasil diinsert")
