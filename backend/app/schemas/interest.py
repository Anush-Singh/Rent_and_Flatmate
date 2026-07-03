from pydantic import BaseModel


class InterestCreate(BaseModel):
    tenant_id: int
    listing_id: int