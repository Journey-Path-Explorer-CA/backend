import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from trip.schema.TripSchema import TripS

df = pd.read_csv("trips.txt")

db: Session = SessionLocal()

for _, row in df.iterrows():
    trip = TripS(
        trip_id=row["trip_id"],
        route_id=row["route_id"],
        service_id=row["service_id"],
        trip_headsign=row.get("trip_headsign", ""),
        trip_short_name=row.get("trip_short_name", ""),
        direction_id=int(row.get("direction_id", 0)),
        shape_id=row["shape_id"]
    )
    db.add(trip)

db.commit()
db.close()
print("Datos de trips importados exitosamente.")
