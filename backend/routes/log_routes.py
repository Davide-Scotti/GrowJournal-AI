from fastapi import APIRouter, UploadFile, Form 
from typing import List, Optional
from models.log_model import GrowLog
from utils.file_utils import save_image
from datetime import datetime

router = APIRouter()

# Mock database in memoria
logs = []

@router.post("/logs")
async def create_log(
    note: str = Form(...),
    date: Optional[str] = Form(None),
    temperature: Optional[float] = Form(None),
    humidity: Optional[float] = Form(None),
    lightHours: Optional[float] = Form(None),
    image: Optional[UploadFile] = None
):

    image_name = save_image(image) if image else None
    log = GrowLog(
        date=datetime.fromisoformat(date) if date else datetime.now(),
        note=note,
        temperature=temperature,
        humidity=humidity,
        light_hours=light_hours
    )
    entry = log.dict()
    entry["image"] = image_name
    logs.append(entry)
    return {"message": "Log saved", "data": entry}

@router.post("/log")
def add_log(entry: dict):
    return {"status": "ok", "log": entry}

@router.get("/")
def read_root():
    return {"message": "GrowJournal API attiva!"}