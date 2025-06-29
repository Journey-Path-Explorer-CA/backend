import pandas as pd
from stoptime.schema.StopTimeSchema import StopTimeS
from database import SessionLocal
from sqlalchemy.exc import IntegrityError

df = pd.read_csv("stop_times.txt", encoding="utf-8-sig", sep=",")

db = SessionLocal()

stop_times = []
for _, row in df.iterrows():
    stop_time = StopTimeS(
        trip_id=row["trip_id"],
        timepoint=row["timepoint"],
        stop_id=row["stop_id"],
        stop_sequence=row["stop_sequence"],
        arrival_time=row["arrival_time"],
        departure_time=row["departure_time"]
    )
    stop_times.append(stop_time)

try:
    db.bulk_save_objects(stop_times)
    db.commit()
    print(f"{len(stop_times)} registros cargados correctamente en stop_times.")
except IntegrityError as e:
    db.rollback()
    print("Error de integridad:", e)
finally:
    db.close()