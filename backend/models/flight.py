from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.database import Base
from datetime import datetime

class FlightModel(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    duration = Column(Float, nullable=True)
    max_speed = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    telemetry_data = Column(Text)  # JSON-строка
    video_path = Column(String, nullable=True)
    voltage_avg = Column(Float)
    rssi_min = Column(Integer)