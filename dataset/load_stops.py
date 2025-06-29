import pandas as pd
from stop.schema.StopSchema import StopS
from database import SessionLocal
from sqlalchemy.exc import IntegrityError

def load_data():
    df = pd.read_csv("stops.txt", encoding="utf-8-sig", sep=",")
    db = SessionLocal()
    new_stops = []
    for _, row in df.iterrows():
        exists = db.query(StopS).filter_by(stop_id=row["stop_id"]).first()
        if not exists:
            stop = StopS(
                stop_id=row["stop_id"],
                stop_name=row["stop_name"],
                stop_lat=row["stop_lat"],
                stop_lon=row["stop_lon"],
                zone_id=row["zone_id"],
                wheelchair_boarding=row["wheelchair_boarding"]
            )
            new_stops.append(stop)
    try:
        db.bulk_save_objects(new_stops)
        db.commit()
        print(f"✅ {len(new_stops)} stops nuevos cargados correctamente desde stops.txt.")
    except IntegrityError as e:
        db.rollback()
        print("❌ Error de integridad:", e)
    finally:
        db.close()
