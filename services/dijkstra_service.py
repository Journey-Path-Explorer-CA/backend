from sqlalchemy.orm import Session
import networkx as nx
from stop.schema.StopSchema import StopS
from services.graph_service import build_graph

def dijkstra_route(db: Session, start_id: str, end_id: str):
    G = build_graph(db)
    if start_id not in G or end_id not in G:
        return None
    try:
        path = nx.dijkstra_path(G, source=start_id, target=end_id, weight="weight")
        total_distance = sum(G[u][v]["weight"] for u, v in zip(path[:-1], path[1:]))
        stops = db.query(StopS).filter(StopS.stop_id.in_(path)).all()
        stop_map = {s.stop_id: s for s in stops}
        sequence = [{
            "stop_id": sid,
            "stop_name": stop_map[sid].stop_name,
            "stop_lat": stop_map[sid].stop_lat,
            "stop_lon": stop_map[sid].stop_lon,
            "wheelchair_boarding": stop_map[sid].wheelchair_boarding
        } for sid in path if sid in stop_map]
        return {"sequence": sequence, "total_distance": total_distance}
    except nx.NetworkXNoPath:
        return None

def dijkstra_distance(db: Session, start_id: str, end_id: str):
    G = build_graph(db)
    if start_id not in G or end_id not in G:
        return None
    try:
        path = nx.dijkstra_path(G, source=start_id, target=end_id, weight="weight")
        return {"total_distance": sum(G[u][v]["weight"] for u, v in zip(path[:-1], path[1:]))}
    except nx.NetworkXNoPath:
        return None