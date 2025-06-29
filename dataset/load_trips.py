import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from trip.schema.TripSchema import TripS
from sqlalchemy.exc import IntegrityError

def load_data():
    df = pd.read_csv("trips.txt")
    db: Session = SessionLocal()
    new_trips = []
    for _, row in df.iterrows():
        exists = db.query(TripS).filter_by(trip_id=row["trip_id"]).first()
        if not exists:
            trip = TripS(
                trip_id=row["trip_id"],
                route_id=row["route_id"],
                service_id=row["service_id"],
                trip_headsign=row.get("trip_headsign", ""),
                trip_short_name=row.get("trip_short_name", ""),
                direction_id=int(row.get("direction_id", 0)),
                shape_id=row["shape_id"]
            )
            new_trips.append(trip)
    try:
        db.bulk_save_objects(new_trips)
        db.commit()
        print(f"✅ {len(new_trips)} trips nuevos cargados correctamente desde trips.txt.")
    except IntegrityError as e:
        db.rollback()
        print("❌ Error de integridad:", e)
    finally:
        db.close()
