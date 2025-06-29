import pandas as pd
from stoptime.schema.StopTimeSchema import StopTimeS
from database import SessionLocal
from sqlalchemy.exc import IntegrityError

# 📂 Lee el archivo directamente
df = pd.read_csv("stop_times.txt", encoding="utf-8-sig", sep=",")

# 🗃️ Abre la sesión
db = SessionLocal()

# 🚀 Crea todos los objetos SIN verificar duplicados
new_stop_times = [
    StopTimeS(
        trip_id=row["trip_id"],
        timepoint=row["timepoint"],
        stop_id=row["stop_id"],
        stop_sequence=row["stop_sequence"],
        arrival_time=row["arrival_time"],
        departure_time=row["departure_time"]
    )
    for _, row in df.iterrows()
]

# ✅ Guarda en la base de datos
try:
    db.bulk_save_objects(new_stop_times)
    db.commit()
    print(f"✅ {len(new_stop_times)} registros cargados rápidamente en stop_times.")
except IntegrityError as e:
    db.rollback()
    print("❌ Error de integridad:", e)
finally:
    db.close()
