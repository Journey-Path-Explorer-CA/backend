from fastapi import APIRouter, HTTPException, status
from configuration.db_dependency import db_dependency
from trip.model.aggregates.Trip import Trip
from trip.schema.TripSchema import TripS

trip = APIRouter()

@trip.post("/trips/", status_code=status.HTTP_201_CREATED, tags=["Trips"])
async def create_trip(data: Trip, db: db_dependency):
    db_trip = TripS(**data.dict())
    db.add(db_trip)
    db.commit()
    return {"message": "Trip created successfully"}

@trip.get("/trips/", tags=["Trips"])
async def get_all_trips(db: db_dependency):
    return db.query(TripS).all()

@trip.get("/trips/{trip_id}", tags=["Trips"])
async def get_trip_by_id(trip_id: str, db: db_dependency):
    trip_obj = db.query(TripS).filter(TripS.trip_id == trip_id).first()
    if not trip_obj:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip_obj

@trip.put("/trips/{trip_id}", tags=["Trips"])
async def update_trip(trip_id: str, data: Trip, db: db_dependency):
    trip_obj = db.query(TripS).filter(TripS.trip_id == trip_id).first()
    if not trip_obj:
        raise HTTPException(status_code=404, detail="Trip not found")
    for key, value in data.dict().items():
        setattr(trip_obj, key, value)
    db.commit()
    return {"message": "Trip updated successfully"}

@trip.delete("/trips/{trip_id}", tags=["Trips"])
async def delete_trip(trip_id: str, db: db_dependency):
    trip_obj = db.query(TripS).filter(TripS.trip_id == trip_id).first()
    if not trip_obj:
        raise HTTPException(status_code=404, detail="Trip not found")
    db.delete(trip_obj)
    db.commit()
    return {"message": "Trip deleted successfully"}

@trip.get("/trips/by_service/{service_id}", tags=["Trips"])
async def get_trips_by_service_id(service_id: str, db: db_dependency):
    trips = db.query(TripS).filter(TripS.service_id == service_id).all()
    if not trips:
        raise HTTPException(status_code=404, detail="No trips found for the given service_id")

    result = [
        {
            "trip_id": trip.trip_id,
            "route_id": trip.route_id,
            "trip_headsign": trip.trip_headsign,
            "trip_short_name": trip.trip_short_name,
            "direction_id": trip.direction_id,
            "shape_id": trip.shape_id
        }
        for trip in trips
    ]
    return result