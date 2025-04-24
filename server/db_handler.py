from data.session import SessionLocal
from data.repository import VehicleRepository


class DBHandler:
    def __init__(self):
        self.session = SessionLocal()
        self.repository = VehicleRepository(self.session)

    def get_filtered_vehicles(self, filters: dict):
        return self.repository.filter_by(filters)

    def close(self):
        self.session.close()
