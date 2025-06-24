from pydantic import BaseModel

class Shape(BaseModel):
    shape_id: str
    shape_pt_sequence: int
    shape_dist_traveled: float
