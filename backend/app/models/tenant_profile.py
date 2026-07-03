from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base

class TenantProfile(Base):
    __tablename__ = "tenant_profiles"

    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer)
    preferred_location = Column(String)
    budget_min = Column(Integer)
    budget_max = Column(Integer)
    move_in_date = Column(Date)