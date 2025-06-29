import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from calendarr.schema.CalendarSchema import CalendarS

df = pd.read_csv("calendar.txt")

db: Session = SessionLocal()

for _, row in df.iterrows():
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
    db.add(calendar)

db.commit()
db.close()
print("Datos de calendar importados exitosamente.")
