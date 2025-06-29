import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from shape.schema.ShapeSchema import ShapeS

# 1. Leer archivo
df = pd.read_csv("shapes.txt")

# 2. Limpiar NaN
df = df.dropna(subset=["shape_pt_lat", "shape_pt_lon"])
df["shape_dist_traveled"] = df["shape_dist_traveled"].fillna(0.0)

# 3. Conexión DB
db: Session = SessionLocal()

# 4. Crear lista de objetos (más rápido que db.add() uno por uno)
shapes = []
for _, row in df.iterrows():
    shapes.append(
        ShapeS(
            shape_id=row["shape_id"],
            shape_pt_sequence=int(row["shape_pt_sequence"]),
            shape_pt_lat=float(row["shape_pt_lat"]),
            shape_pt_lon=float(row["shape_pt_lon"]),
            shape_dist_traveled=float(row["shape_dist_traveled"])
        )
    )

# 5. Inserción masiva
db.bulk_save_objects(shapes)
db.commit()
db.close()

print(f"Datos de shapes importados exitosamente: {len(shapes)} filas.")
