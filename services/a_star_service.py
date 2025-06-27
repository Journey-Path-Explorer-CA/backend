from sqlalchemy.orm import Session
from stop.schema.StopSchema import StopS
from services.graph_service import build_graph
from math import radians, cos, sin, sqrt, atan2
import networkx as nx

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def a_star_route(db: Session, start_id: str, end_id: str):
    G = build_graph(db)
    if start_id not in G or end_id not in G:
        return None

    def heuristic(u, v):
        lat1, lon1 = G.nodes[u]["lat"], G.nodes[u]["lon"]
        lat2, lon2 = G.nodes[v]["lat"], G.nodes[v]["lon"]
        return haversine(lat1, lon1, lat2, lon2)

    try:
        path = nx.astar_path(G, source=start_id, target=end_id, heuristic=heuristic, weight="weight")
        total = sum(G[u][v]["weight"] for u, v in zip(path[:-1], path[1:]))
        stops = db.query(StopS).filter(StopS.stop_id.in_(path)).all()
        stop_map = {s.stop_id: s for s in stops}
        sequence = [{
            "stop_id": sid,
            "stop_name": stop_map[sid].stop_name,
            "stop_lat": stop_map[sid].stop_lat,
            "stop_lon": stop_map[sid].stop_lon,
            "wheelchair_boarding": stop_map[sid].wheelchair_boarding
        } for sid in path if sid in stop_map]
        return {"sequence": sequence, "total_distance": total}
    except nx.NetworkXNoPath:
        return None

def a_star_distance(db: Session, start_id: str, end_id: str):
    G = build_graph(db)
    if start_id not in G or end_id not in G:
        return None

    def heuristic(u, v):
        lat1, lon1 = G.nodes[u]["lat"], G.nodes[u]["lon"]
        lat2, lon2 = G.nodes[v]["lat"], G.nodes[v]["lon"]
        return haversine(lat1, lon1, lat2, lon2)

    try:
        path = nx.astar_path(G, source=start_id, target=end_id, heuristic=heuristic, weight="weight")
        total = sum(G[u][v]["weight"] for u, v in zip(path[:-1], path[1:]))
        return {"total_distance": total}
    except nx.NetworkXNoPath:
        return None