from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DB_URL = 'postgresql://postgres:adminadmin@localhost/fastapi_wildberies_ai32'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass



