import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from trip.schema.TripSchema import TripS
from sqlalchemy.exc import IntegrityError

# 📂 Lee el archivo directamente
df = pd.read_csv("trips.txt")

# 🗃️ Abre la sesión
db: Session = SessionLocal()

# 🚀 Procesa todos los registros SIN verificación de existencia
new_trips = [
    TripS(
        trip_id=row["trip_id"],
        route_id=row["route_id"],
        service_id=row["service_id"],
        trip_headsign=row.get("trip_headsign", ""),
        trip_short_name=row.get("trip_short_name", ""),
        direction_id=int(row.get("direction_id", 0)),
        shape_id=row["shape_id"]
    )
    for _, row in df.iterrows()
]

# ✅ Guarda en la base de datos
try:
    db.bulk_save_objects(new_trips)
    db.commit()
    print(f"✅ {len(new_trips)} trips cargados rápidamente desde trips.txt.")
except IntegrityError as e:
    db.rollback()
    print("❌ Error de integridad:", e)
finally:
    db.close()
