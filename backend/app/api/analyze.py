from fastapi import APIRouter
from app.services.ai_analyzer import detect_smoothness_errors

router = APIRouter()

@router.get("/analyze/{flight_id}")
async def analyze_flight(flight_id: int):
    # Здесь загружаем данные из БД
    telemetry = [{"ax": 1, "ay": 2, "az": 3, "gx": 4, "gy": 5, "gz": 6, "voltage": 16.8} for _ in range(100)]
    result = detect_smoothness_errors(telemetry)
    return result