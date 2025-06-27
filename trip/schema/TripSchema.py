from sqlalchemy import Column, String, Integer
from database import Base

class TripS(Base):
    __tablename__ = "trips"

    trip_id = Column(String(100), primary_key=True)
    route_id = Column(String(100), nullable=False)
    service_id = Column(String(100), nullable=False)
    trip_headsign = Column(String(255), nullable=True)
    trip_short_name = Column(String(255), nullable=True)
    direction_id = Column(Integer, nullable=True)
    shape_id = Column(String(100), nullable=False)
