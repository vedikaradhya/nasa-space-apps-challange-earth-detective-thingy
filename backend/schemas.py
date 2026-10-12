from pydantic import BaseModel
from typing import List, Dict

class TrendPayload(BaseModel):
    data: List[Dict]

    class Config:
        extra = "allow"
