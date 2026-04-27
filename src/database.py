from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Usaremos SQLite como base de datos local
DATABASE_URL = "sqlite:///contimusic.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
