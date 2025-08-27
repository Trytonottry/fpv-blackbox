from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload, flights, analyze
from app.database import init_db

app = FastAPI(title="FPV Blackbox Backend", version="1.0")

# Инициализация БД
init_db()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Роуты
app.include_router(upload.router, prefix="/api")
app.include_router(flights.router, prefix="/api")
app.include_router(analyze.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "FPV Blackbox API is running", "docs": "/docs"}