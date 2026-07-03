from pydantic import BaseModel
from datetime import date


class ListingCreate(BaseModel):
    owner_id: int
    location: str
    rent: int
    available_from: date
    room_type: str
    furnishing_status: str