from pydantic import BaseModel

class StopTime(BaseModel):
    stop_id: str
    stop_sequence: int
    arrival_time: str
