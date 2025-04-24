from faker import Faker
import random
from .models import Vehicle
from .repository import VehicleRepository
from .session import SessionLocal, init_db

fake = Faker()

BRANDS = ["Toyota", "Honda", "Ford",
          "Chevrolet", "BMW", "Volkswagen", "Hyundai"]
MODELS = ["Sedan", "Hatchback", "SUV", "Coupe", "Pickup"]
ENGINES = ["1.0", "1.4", "1.6", "2.0", "V6", "V8"]
FUELS = ["Gasoline", "Ethanol", "Diesel", "Electric"]
COLORS = ["Red", "Blue", "Black", "White", "Silver", "Gray"]
TRANSMISSIONS = ["Manual", "Automatic"]


def generate_vehicle() -> Vehicle:
    return Vehicle(
        brand=random.choice(BRANDS),
        model=random.choice(MODELS),
        year=random.randint(2005, 2023),
        engine=random.choice(ENGINES),
        fuel=random.choice(FUELS),
        color=random.choice(COLORS),
        mileage=random.randint(10000, 150000),
        doors=random.choice([2, 4]),
        transmission=random.choice(TRANSMISSIONS),
        price=round(random.uniform(25000, 150000), 2),
    )


def main():
    init_db()
    session = SessionLocal()
    repo = VehicleRepository(session)

    for _ in range(100):
        vehicle = generate_vehicle()
        repo.add(vehicle)

    print("Database successfully populated with fake vehicles.")


if __name__ == "__main__":
    main()
