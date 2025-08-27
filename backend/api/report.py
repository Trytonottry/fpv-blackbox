from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.services.pdf_report import generate_pdf_report

router = APIRouter()

@router.get("/report/{flight_id}")
def get_pdf_report(flight_id: int):
    # Здесь загружаем flight_data и analysis
    path = f"/app/data/reports/flight_{flight_id}.pdf"
    generate_pdf_report(flight_data, analysis, path)
    return FileResponse(path, media_type='application/pdf', filename=f"flight_{flight_id}.pdf")