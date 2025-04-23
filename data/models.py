from dataclasses import dataclass, field
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import registry

mapper_registry = registry()

@mapper_registry.mapped
@dataclass
class Vehicle:
  __tablename__ = "vehicles"
  __sa_dataclass_metadata_key__ = "sa"

  id: int = field(init=False, metadata={"sa": Column(Integer, primary_key=True, autoincrement=True)})
  brand: str = field(metadata={"sa": Column(String(50), nullable=False)})
  model: str = field(metadata={"sa": Column(String(50), nullable=False)})
  year: int = field(metadata={"sa": Column(Integer, nullable=False)})
  engine: str = field(metadata={"sa": Column(String(30), nullable=False)})
  fuel: str = field(metadata={"sa": Column(String(30), nullable=False)})
  color: str = field(metadata={"sa": Column(String(30), nullable=False)})
  mileage: int = field(metadata={"sa": Column(Integer, nullable=False)})
  doors: int = field(metadata={"sa": Column(Integer, nullable=False)})
  transmission: str = field(metadata={"sa": Column(String(30), nullable=False)})
  price: float = field(metadata={"sa": Column(Float, nullable=False)})
