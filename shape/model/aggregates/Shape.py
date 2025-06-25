from pydantic import BaseModel

class Shape(BaseModel):
    shape_id: str
    shape_pt_sequence: int
    shape_pt_lat: float
    shape_pt_lon: float
    shape_dist_traveled: float
