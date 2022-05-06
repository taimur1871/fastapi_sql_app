# Library imports
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, func

Base = declarative_base()


# Here we define our ORM objects using SqlAlchemy
class BaseTemporal(Base):
    __abstract__ = True
    created = Column(DateTime(timezone=True), default=func.now(), nullable=False, index=True)


class BitData(Base):
    __tablename__ = 'bit_data'

    id = Column(Integer, default=None, primary_key=True, nullable=False)
    bit_name = Column(String, default=None, nullable=False)
    bit_size = Column(Float, default=0, nullable=False)
    bit_type = Column(String, default="", nullable=False)
    mfg = Column(String, default="", nullable=False)
    serial_no = Column(String, default="", nullable=False)
    depth_in = Column(Float, default=0.0, nullable=True)
    depth_out = Column(Float, default=0.0, nullable=True)
    distance = Column(Float, default=0.0, nullable=True)
    hours = Column(Float, default=0.0, nullable=True)
    rop = Column(Float, default=0.0, nullable=True)


class WellData(Base):
    __tablename__ = 'well_data'

    id = Column(Integer, default=None, primary_key=True, nullable=False)
    well_name = Column(String, default="")
    operator = Column(String, default="")
    lat = Column(Float, default=0.0)
    lon = Column(Float, default=0.0)


class Manufacturer(Base):
    __tablename__ = 'manufacturer'

    id = Column(Integer, default=None, primary_key=True, nullable=False)
    mfg_name = Column(String, default="", nullable=True)


class DullGrade(Base):
    __tablename__ = 'dull_grade'

    id = Column(Integer, default=None, primary_key=True, nullable=False)
    grade = Column(String, default="", nullable=True)
    inner = Column(Integer, default=0, nullable=True)
    outer = Column(Integer, default=0, nullable=True)
    main = Column(String, default="", nullable=True)
    loc = Column(String, default="", nullable=True)
    bearing = Column(String, default="X", nullable=True)
    gauge = Column(Float, default=0.0, nullable=True)
    other = Column(String, default="", nullable=True)
    reason_pulled = Column(String, default="", nullable=True)


if __name__ == '__main__':
    pass
