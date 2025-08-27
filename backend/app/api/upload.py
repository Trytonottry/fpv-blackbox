from fastapi import APIRouter, File, UploadFile
from app.services.parser import parse_log_file
from app.services.video_processor import extract_frames
import os

router = APIRouter()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_flight_data(log_file: UploadFile = File(...), video_file: UploadFile = File(None)):
    log_path = f"{UPLOAD_DIR}/{log_file.filename}"
    with open(log_path, "wb") as f:
        f.write(await log_file.read())

    data = parse_log_file(log_path)

    if video_file:
        video_path = f"{UPLOAD_DIR}/{video_file.filename}"
        with open(video_path, "wb") as f:
            f.write(await video_file.read())
        extract_frames(video_path, "data/frames")

    return {"status": "uploaded", "telemetry": data[:5], "total_points": len(data)}