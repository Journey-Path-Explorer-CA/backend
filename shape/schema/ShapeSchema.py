from sqlalchemy import Column, String, Float, Integer
from database import Base

class ShapeS(Base):
    __tablename__ = "shapes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    shape_id = Column(String(100), nullable=False)
    shape_pt_sequence = Column(Integer, nullable=False)
    shape_pt_lat = Column(Float, nullable=False)
    shape_pt_lon = Column(Float, nullable=False)
    shape_dist_traveled = Column(Float, nullable=False)
