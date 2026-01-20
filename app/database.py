from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./data.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class SensorLog(Base):
    __tablename__ = "sensor_log"

    id = Column(Integer, primary_key=True, index=True)
    lokasi = Column(String)
    suhu = Column(Float)
    kelembapan = Column(Float)

Base.metadata.create_all(bind=engine)
