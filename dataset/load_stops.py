import pandas as pd
from stop.schema.StopSchema import StopS
from database import SessionLocal
from sqlalchemy.exc import IntegrityError

df = pd.read_csv("stops.txt", encoding="utf-8-sig", sep=",")

db = SessionLocal()

stops = []
for _, row in df.iterrows():
    stop = StopS(
        stop_id=row["stop_id"],
        stop_name=row["stop_name"],
        stop_lat=row["stop_lat"],
        stop_lon=row["stop_lon"],
        zone_id=row["zone_id"],
        wheelchair_boarding=row["wheelchair_boarding"]
    )
    stops.append(stop)

try:
    db.bulk_save_objects(stops)
    db.commit()
    print(f"{len(stops)} stops cargados correctamente desde stops.txt.")
except IntegrityError as e:
    db.rollback()
    print("Error de integridad:", e)
finally:
    db.close()