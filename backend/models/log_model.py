from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GrowLog(BaseModel):
    date: datetime
    note: str
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    lightHours: Optional[float] = None