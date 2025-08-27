from fastapi import APIRouter
from app.database import SessionLocal
from app.models.flight import FlightModel

router = APIRouter()

@router.get("/flights")
def get_flights():
    db = SessionLocal()
    flights = db.query(FlightModel).all()
    db.close()
    return [{"id": f.id, "filename": f.filename, "duration": f.duration, "created": f.created_at} for f in flights]

@router.get("/flights/{flight_id}")
def get_flight(flight_id: int):
    db = SessionLocal()
    flight = db.query(FlightModel).filter(FlightModel.id == flight_id).first()
    db.close()
    if not flight:
        return {"error": "Not found"}
    return {
        "id": flight.id,
        "telemetry": json.loads(flight.telemetry_data),
        "video": flight.video_path,
        "stats": {
            "voltage_avg": flight.voltage_avg,
            "rssi_min": flight.rssi_min
        }
    }