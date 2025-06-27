from sqlalchemy.orm import Session
import networkx as nx
from stop.schema.StopSchema import StopS
from stoptime.schema.StopTimeSchema import StopTimeS
from trip.schema.TripSchema import TripS
from shape.schema.ShapeSchema import ShapeS
from sqlalchemy import asc
from itertools import groupby

def build_graph(db: Session) -> nx.DiGraph:
    G = nx.DiGraph()
    stops = db.query(StopS).all()
    for stop in stops:
        G.add_node(stop.stop_id, label=stop.stop_name, lat=stop.stop_lat, lon=stop.stop_lon)
    trips = db.query(TripS).all()
    trip_shape_map = {trip.trip_id: trip.shape_id for trip in trips}
    stop_times = db.query(StopTimeS).order_by(asc(StopTimeS.trip_id), asc(StopTimeS.stop_sequence)).all()
    shape_data = db.query(ShapeS).order_by(asc(ShapeS.shape_id), asc(ShapeS.shape_pt_sequence)).all()
    shape_map = {}
    for shape in shape_data:
        shape_map.setdefault(shape.shape_id, []).append(shape.shape_dist_traveled)
    for trip_id, group in groupby(stop_times, key=lambda x: x.trip_id):
        group = list(group)
        shape_id = trip_shape_map.get(trip_id)
        if not shape_id or shape_id not in shape_map:
            continue
        distances = shape_map[shape_id]
        for i in range(len(group) - 1):
            try:
                G.add_edge(group[i].stop_id, group[i + 1].stop_id, weight=distances[i + 1] - distances[i])
            except IndexError:
                continue
    return G