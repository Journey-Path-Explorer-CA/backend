from sqlalchemy import Column, String, Integer
from database import Base

class StopTimeS(Base):
    __tablename__ = "stop_times"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stop_id = Column(String(100), nullable=False)
    stop_sequence = Column(Integer, nullable=False)
    arrival_time = Column(String(8), nullable=False)  # Puede ser "08:00:00"
