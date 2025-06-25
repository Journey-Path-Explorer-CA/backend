from fastapi import FastAPI
from database import Base, engine
# Importa tus routers
from shape.route.ShapesController import shape
from stop.route.StopsController import stop
from stoptime.route.StopTimesController import stop_time
from trip.route.TripsController import trip
from route.graph_controller import graph_router
app = FastAPI()

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(stop)
app.include_router(stop_time)
app.include_router(shape)
app.include_router(graph_router)
app.include_router(trip)