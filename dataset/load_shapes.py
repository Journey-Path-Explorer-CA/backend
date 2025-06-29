import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal
from shape.schema.ShapeSchema import ShapeS
from sqlalchemy.exc import IntegrityError

def load_data():
    df = pd.read_csv("shapes.txt")
    df = df.dropna(subset=["shape_pt_lat", "shape_pt_lon"])
    df["shape_dist_traveled"] = df["shape_dist_traveled"].fillna(0.0)
    db: Session = SessionLocal()
    new_shapes = []
    for _, row in df.iterrows():
        exists = db.query(ShapeS).filter_by(
            shape_id=row["shape_id"],
            shape_pt_sequence=int(row["shape_pt_sequence"])
        ).first()
        if not exists:
            new_shapes.append(
                ShapeS(
                    shape_id=row["shape_id"],
                    shape_pt_sequence=int(row["shape_pt_sequence"]),
                    shape_pt_lat=float(row["shape_pt_lat"]),
                    shape_pt_lon=float(row["shape_pt_lon"]),
                    shape_dist_traveled=float(row["shape_dist_traveled"])
                )
            )
    try:
        db.bulk_save_objects(new_shapes)
        db.commit()
        print(f"✅ Datos de shapes importados exitosamente: {len(new_shapes)} nuevos registros.")
    except IntegrityError as e:
        db.rollback()
        print("❌ Error de integridad:", e)
    finally:
        db.close()
