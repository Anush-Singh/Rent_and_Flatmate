from sqlalchemy import Column, Integer, String
from app.db.database import Base

class CompatibilityScore(Base):
    __tablename__ = "compatibility_scores"

    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer)
    listing_id = Column(Integer)
    score = Column(Integer)
    explanation = Column(String)