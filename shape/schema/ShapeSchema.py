from sqlalchemy import Column, String, Integer, Float
from database import Base

class ShapeS(Base):
    __tablename__ = "shapes"

    shape_id = Column(String(100), primary_key=True)  # identificador único
    shape_pt_sequence = Column(Integer, nullable=False)
    shape_dist_traveled = Column(Float, nullable=False)