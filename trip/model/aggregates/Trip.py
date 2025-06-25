from pydantic import BaseModel

class Trip(BaseModel):
    route_id: str
    service_id: str
    trip_id: str
    trip_headsign: str
    trip_short_name: str
    direction_id: int
    shape_id: str
