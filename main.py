from fastapi import FastAPI
from database import Base, engine
# Importa tus routers
from shape.route.ShapesController import shape
from stop.route.StopsController import stop
from stoptime.route.StopTimesController import stop_time
from trip.route.TripsController import trip
from route.graph_controller import graph_router
from calendarr.route.CalendarController import calendar

import dataset.load_calendar as load_calendar
import dataset.load_shapes as load_shapes
import dataset.load_stop_times as load_stop_times
import dataset.load_stops as load_stops
import dataset.load_trips as load_trips
app = FastAPI()

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(stop)
app.include_router(stop_time)
app.include_router(shape)
app.include_router(graph_router)
app.include_router(trip)
app.include_router(calendar)

@app.on_event("startup")
def startup_event():
    load_calendar.load_data()
    load_shapes.load_data()
    load_stop_times.load_data()
    load_stops.load_data()
    load_trips.load_data()