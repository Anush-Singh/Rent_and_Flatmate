from sqlalchemy import Column, Integer, String, Date, Boolean
from app.db.database import Base


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    location = Column(String)
    rent = Column(Integer)
    available_from = Column(Date)
    room_type = Column(String)
    furnishing_status = Column(String)
    filled = Column(Boolean, default=False)