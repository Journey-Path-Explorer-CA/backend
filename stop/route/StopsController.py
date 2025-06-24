from fastapi import APIRouter, HTTPException, status
from configuration.db_dependency import db_dependency
from stop.model.aggregates.Stop import Stop
from stop.schema.StopSchema import StopS

stop = APIRouter()

@stop.post("/stops/", status_code=status.HTTP_201_CREATED, tags=["Stops"])
async def create_stop(stop_data: Stop, db: db_dependency):
    db_stop = StopS(**stop_data.dict())
    db.add(db_stop)
    db.commit()
    return {"message": "Stop creado correctamente"}

@stop.get("/stops/", tags=["Stops"])
async def get_all_stops(db: db_dependency):
    return db.query(StopS).all()

@stop.get("/stops/{stop_id}", tags=["Stops"])
async def get_stop_by_id(stop_id: str, db: db_dependency):
    stop = db.query(StopS).filter(StopS.stop_id == stop_id).first()
    if not stop:
        raise HTTPException(status_code=404, detail="Stop no encontrado")
    return stop

@stop.put("/stops/{stop_id}", tags=["Stops"])
async def update_stop(stop_id: str, stop_data: Stop, db: db_dependency):
    db_stop = db.query(StopS).filter(StopS.stop_id == stop_id).first()
    if not db_stop:
        raise HTTPException(status_code=404, detail="Stop no encontrado")
    for key, value in stop_data.dict().items():
        setattr(db_stop, key, value)
    db.commit()
    return {"message": "Stop actualizado correctamente"}

@stop.delete("/stops/{stop_id}", tags=["Stops"])
async def delete_stop(stop_id: str, db: db_dependency):
    db_stop = db.query(StopS).filter(StopS.stop_id == stop_id).first()
    if not db_stop:
        raise HTTPException(status_code=404, detail="Stop no encontrado")
    db.delete(db_stop)
    db.commit()
    return {"message": "Stop eliminado correctamente"}
