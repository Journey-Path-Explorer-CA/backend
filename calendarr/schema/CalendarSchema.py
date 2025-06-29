from sqlalchemy import Column, String, Integer
from database import Base

class CalendarS(Base):
    __tablename__ = "calendar"

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(String(20), nullable=False, unique=True)
    monday = Column(Integer, nullable=False)
    tuesday = Column(Integer, nullable=False)
    wednesday = Column(Integer, nullable=False)
    thursday = Column(Integer, nullable=False)
    friday = Column(Integer, nullable=False)
    saturday = Column(Integer, nullable=False)
    sunday = Column(Integer, nullable=False)
    start_date = Column(String(8), nullable=False)
    end_date = Column(String(8), nullable=False)
