from pydantic import BaseModel

class Stop(BaseModel):
    stop_id: str
    stop_name: str
    wheelchair_boarding: int
