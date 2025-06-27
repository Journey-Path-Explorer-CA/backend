from fastapi import APIRouter, HTTPException, status
from configuration.db_dependency import db_dependency
from shape.model.aggregates.Shape import Shape
from shape.schema.ShapeSchema import ShapeS

shape = APIRouter()

@shape.post("/shapes/", status_code=status.HTTP_201_CREATED, tags=["Shapes"])
async def create_shape(data: Shape, db: db_dependency):
    db_obj = ShapeS(**data.dict())
    db.add(db_obj)
    db.commit()
    return {"message": "Shape created successfully"}

@shape.get("/shapes/", tags=["Shapes"])
async def get_all_shapes(db: db_dependency):
    return db.query(ShapeS).all()

@shape.get("/shapes/{id}", tags=["Shapes"])
async def get_shape(id: int, db: db_dependency):
    obj = db.query(ShapeS).filter(ShapeS.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Shape not found")
    return obj

@shape.put("/shapes/{id}", tags=["Shapes"])
async def update_shape(id: int, data: Shape, db: db_dependency):
    obj = db.query(ShapeS).filter(ShapeS.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Shape not found")
    for k, v in data.dict().items():
        setattr(obj, k, v)
    db.commit()
    return {"message": "Shape updated successfully"}

@shape.delete("/shapes/{id}", tags=["Shapes"])
async def delete_shape(id: int, db: db_dependency):
    obj = db.query(ShapeS).filter(ShapeS.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Shape not found")
    db.delete(obj)
    db.commit()
    return {"message": "Shape deleted successfully"}