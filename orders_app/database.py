import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f'sqlite:///{os.path.join(BASE_DIR, "orders.db")}')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()