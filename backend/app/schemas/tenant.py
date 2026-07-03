from pydantic import BaseModel
from datetime import date


class TenantProfileCreate(BaseModel):
    tenant_id: int
    preferred_location: str
    budget_min: int
    budget_max: int
    move_in_date: date