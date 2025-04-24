from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from .models import Vehicle


class VehicleRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, vehicle: Vehicle) -> None:
        self.session.add(vehicle)
        self.session.commit()

    def get_all(self) -> List[Vehicle]:
        return self.session.query(Vehicle).all()

    def get_by_id(self, vehicle_id: int) -> Optional[Vehicle]:
        return self.session.query(Vehicle).filter_by(id=vehicle_id).first()

    def filter_by(self, filters: Dict[str, Any]) -> List[Vehicle]:
        query = self.session.query(Vehicle)
        for attr, value in filters.items():
            if hasattr(Vehicle, attr):
                query = query.filter(getattr(Vehicle, attr) == value)
        return query.all()
