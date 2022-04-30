from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from app.core import config
#
# engine = create_engine(
#     config.SQLALCHEMY_DATABASE_URI,
# )

data_engine = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost:5432/bit_data'
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=data_engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
