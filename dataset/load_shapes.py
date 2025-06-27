import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from shape.schema.ShapeSchema import ShapeS

df = pd.read_csv("shapes.txt")

df = df.dropna(subset=["shape_pt_lat", "shape_pt_lon"])
df["shape_dist_traveled"] = df["shape_dist_traveled"].fillna(0.0)

db: Session = SessionLocal()

for _, row in df.iterrows():
    shape = ShapeS(
        shape_id=row["shape_id"],
        shape_pt_sequence=int(row["shape_pt_sequence"]),
        shape_pt_lat=float(row["shape_pt_lat"]),
        shape_pt_lon=float(row["shape_pt_lon"]),
        shape_dist_traveled=float(row["shape_dist_traveled"])
    )
    db.add(shape)

db.commit()
db.close()
print("Datos de shapes importados exitosamente.")