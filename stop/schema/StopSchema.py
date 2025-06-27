from sqlalchemy import Column, String, Float, Integer
from database import Base

class StopS(Base):
    __tablename__ = "stops"

    stop_id = Column(String(100), primary_key=True)
    stop_name = Column(String(100), nullable=False)
    stop_lat = Column(Float, nullable=False)
    stop_lon = Column(Float, nullable=False)
    zone_id = Column(String(100), nullable=False)
    wheelchair_boarding = Column(Integer, nullable=False)
