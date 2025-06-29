import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from calendarr.schema.CalendarSchema import CalendarS
from sqlalchemy.exc import IntegrityError

def load_data():
    df = pd.read_csv("calendar.txt")
    db: Session = SessionLocal()
    new_rows = []
    for _, row in df.iterrows():
        exists = db.query(CalendarS).filter_by(service_id=row["service_id"]).first()
        if not exists:
            calendar = CalendarS(
                service_id=row["service_id"],
                monday=row["monday"],
                tuesday=row["tuesday"],
                wednesday=row["wednesday"],
                thursday=row["thursday"],
                friday=row["friday"],
                saturday=row["saturday"],
                sunday=row["sunday"],
                start_date=row["start_date"],
                end_date=row["end_date"]
            )
            new_rows.append(calendar)
    try:
        db.bulk_save_objects(new_rows)
        db.commit()
        print(f"✅ Datos de calendar importados exitosamente: {len(new_rows)} nuevos registros.")
    except IntegrityError as e:
        db.rollback()
        print("❌ Error de integridad:", e)
    finally:
        db.close()
