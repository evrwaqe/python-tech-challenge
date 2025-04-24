from .models import mapper_registry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DB_PATH", "sqlite:///vehicles.db")

environment_engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=environment_engine,
                            autoflush=False, autocommit=False)


def init_db():
    mapper_registry.metadata.create_all(environment_engine)
