from sqlalchemy import Column, Integer, String
from app.db.database import Base


class InterestRequest(Base):
    __tablename__ = "interest_requests"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer)
    listing_id = Column(Integer)
    status = Column(String, default="Pending")