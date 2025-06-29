import pandas as pd
from stop.schema.StopSchema import StopS
from database import SessionLocal
from sqlalchemy.exc import IntegrityError

# 📂 Lee el archivo directamente
df = pd.read_csv("stops.txt", encoding="utf-8-sig", sep=",")

# 🗃️ Abre la sesión
db = SessionLocal()

# 🚀 Crea todos los objetos SIN verificar duplicados
new_stops = [
    StopS(
        stop_id=row["stop_id"],
        stop_name=row["stop_name"],
        stop_lat=row["stop_lat"],
        stop_lon=row["stop_lon"],
        zone_id=row["zone_id"],
        wheelchair_boarding=row["wheelchair_boarding"]
    )
    for _, row in df.iterrows()
]

# ✅ Guarda en la base de datos
try:
    db.bulk_save_objects(new_stops)
    db.commit()
    print(f"✅ {len(new_stops)} stops cargados rápidamente desde stops.txt.")
except IntegrityError as e:
    db.rollback()
    print("❌ Error de integridad:", e)
finally:
    db.close()
