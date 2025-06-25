from fastapi import APIRouter, HTTPException
from configuration.db_dependency import db_dependency
from services.dijkstra_service import dijkstra_route, dijkstra_distance
from services.a_star_service import a_star_route, a_star_distance
from services.bellman_ford_service import bellman_ford_route, bellman_ford_distance

graph_router = APIRouter()

# --- Dijkstra ---
@graph_router.get("/dijkstra/stops", tags=["Graph"])
def get_dijkstra_sequence(start_stop_id: str, end_stop_id: str, db: db_dependency = None):
    result = dijkstra_route(db, start_stop_id, end_stop_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return result["sequence"]

@graph_router.get("/dijkstra/distance", tags=["Graph"])
def get_dijkstra_distance(start_stop_id: str, end_stop_id: str, db: db_dependency = None):
    result = dijkstra_distance(db, start_stop_id, end_stop_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return result

# --- A* ---
@graph_router.get("/a-star/stops", tags=["Graph"])
def get_astar_sequence(start_stop_id: str, end_stop_id: str, db: db_dependency = None):
    result = a_star_route(db, start_stop_id, end_stop_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return result["sequence"]

@graph_router.get("/a-star/distance", tags=["Graph"])
def get_astar_distance(start_stop_id: str, end_stop_id: str, db: db_dependency = None):
    result = a_star_distance(db, start_stop_id, end_stop_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return result

# --- Bellman-Ford ---
@graph_router.get("/bellman-ford/stops", tags=["Graph"])
def get_bellman_sequence(start_stop_id: str, end_stop_id: str, db: db_dependency = None):
    result = bellman_ford_route(db, start_stop_id, end_stop_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return result["sequence"]

@graph_router.get("/bellman-ford/distance", tags=["Graph"])
def get_bellman_distance(start_stop_id: str, end_stop_id: str, db: db_dependency = None):
    result = bellman_ford_distance(db, start_stop_id, end_stop_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return result