from sqlalchemy import Column, String, Integer
from database import Base

class StopS(Base):
    __tablename__ = "stops"

    stop_id = Column(String(100), primary_key=True)
    stop_name = Column(String(100), nullable=False)
    wheelchair_boarding = Column(Integer, nullable=False)