from pydantic import BaseModel

class StopTime(BaseModel):
    trip_id: str
    timepoint: int
    stop_id: str
    stop_sequence: int
    arrival_time: str
    departure_time: str
