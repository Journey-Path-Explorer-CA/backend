from fastapi import APIRouter, HTTPException, status
from configuration.db_dependency import db_dependency
from calendarr.schema.CalendarSchema import CalendarS

calendar = APIRouter()

@calendar.get("/calendar/services", tags=["Calendar"])
async def get_all_services(db: db_dependency):
    services = db.query(CalendarS).all()
    if not services:
        raise HTTPException(status_code=404, detail="No services found")

    result = [
        {
            "service_id": s.service_id,
            "monday": s.monday,
            "tuesday": s.tuesday,
            "wednesday": s.wednesday,
            "thursday": s.thursday,
            "friday": s.friday,
            "saturday": s.saturday,
            "sunday": s.sunday,
            "start_date": s.start_date,
            "end_date": s.end_date
        }
        for s in services
    ]
    return result