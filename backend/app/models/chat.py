from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base
from datetime import datetime

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer)
    receiver_id = Column(Integer)
    message = Column(String)
    sent_at = Column(DateTime, default=datetime.utcnow)