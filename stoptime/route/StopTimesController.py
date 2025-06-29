from fastapi import APIRouter, HTTPException, status
from configuration.db_dependency import db_dependency
from stop.schema.StopSchema import StopS
from stoptime.model.aggregates.StopTime import StopTime
from stoptime.schema.StopTimeSchema import StopTimeS

stop_time = APIRouter()

@stop_time.post("/stop_times/", status_code=status.HTTP_201_CREATED, tags=["StopTimes"])
async def create_stop_time(data: StopTime, db: db_dependency):
    db_obj = StopTimeS(**data.dict())
    db.add(db_obj)
    db.commit()
    return {"message": "Stop time created successfully"}

@stop_time.get("/stop_times/", tags=["StopTimes"])
async def get_all_stop_times(db: db_dependency):
    return db.query(StopTimeS).all()

@stop_time.get("/stop_times/{id}", tags=["StopTimes"])
async def get_stop_time(id: int, db: db_dependency):
    obj = db.query(StopTimeS).filter(StopTimeS.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Stop time not found")
    return obj

@stop_time.put("/stop_times/{id}", tags=["StopTimes"])
async def update_stop_time(id: int, data: StopTime, db: db_dependency):
    obj = db.query(StopTimeS).filter(StopTimeS.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Stop time not found")
    for k, v in data.dict().items():
        setattr(obj, k, v)
    db.commit()
    return {"message": "Stop time updated successfully"}

@stop_time.delete("/stop_times/{id}", tags=["StopTimes"])
async def delete_stop_time(id: int, db: db_dependency):
    obj = db.query(StopTimeS).filter(StopTimeS.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Stop time not found")
    db.delete(obj)
    db.commit()
    return {"message": "Stop time deleted successfully"}

@stop_time.get("/stop_times/by_trip/{trip_id}", tags=["StopTimes"])
async def get_stops_by_trip_id(trip_id: str, db: db_dependency):
    stop_times = (
        db.query(StopTimeS)
        .filter(StopTimeS.trip_id == trip_id)
        .order_by(StopTimeS.stop_sequence)
        .all()
    )
    if not stop_times:
        raise HTTPException(status_code=404, detail="No stop times found for the given trip_id")

    stop_ids = [st.stop_id for st in stop_times]

    stops = (
        db.query(
            StopS.stop_id,
            StopS.stop_name,
            StopS.stop_lat,
            StopS.stop_lon,
            StopS.zone_id,
            StopS.wheelchair_boarding
        )
        .filter(StopS.stop_id.in_(stop_ids))
        .all()
    )

    return [
        {
            "stop_id": stop.stop_id,
            "stop_name": stop.stop_name,
            "stop_lat": stop.stop_lat,
            "stop_lon": stop.stop_lon,
            "zone_id": stop.zone_id,
            "wheelchair_boarding": stop.wheelchair_boarding
        }
        for stop in stops
    ]
