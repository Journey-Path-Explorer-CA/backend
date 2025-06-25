from pydantic import BaseModel

class Stop(BaseModel):
    stop_id: str
    stop_name: str
    stop_lat: float
    stop_lon: float
    zone_id: str
    wheelchair_boarding: int
