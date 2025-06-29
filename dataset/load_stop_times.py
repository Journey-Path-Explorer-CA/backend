import pandas as pd
from stoptime.schema.StopTimeSchema import StopTimeS
from database import SessionLocal
from sqlalchemy.exc import IntegrityError

def load_data():
    df = pd.read_csv("stop_times.txt", encoding="utf-8-sig", sep=",")
    db = SessionLocal()
    new_stop_times = []
    for _, row in df.iterrows():
        exists = db.query(StopTimeS).filter_by(
            trip_id=row["trip_id"],
            stop_id=row["stop_id"],
            stop_sequence=row["stop_sequence"]
        ).first()
        if not exists:
            stop_time = StopTimeS(
                trip_id=row["trip_id"],
                timepoint=row["timepoint"],
                stop_id=row["stop_id"],
                stop_sequence=row["stop_sequence"],
                arrival_time=row["arrival_time"],
                departure_time=row["departure_time"]
            )
            new_stop_times.append(stop_time)
    try:
        db.bulk_save_objects(new_stop_times)
        db.commit()
        print(f"✅ {len(new_stop_times)} registros nuevos cargados correctamente en stop_times.")
    except IntegrityError as e:
        db.rollback()
        print("❌ Error de integridad:", e)
    finally:
        db.close()
