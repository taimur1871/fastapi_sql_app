# Library imports
from typing import List, Optional
from sqlalchemy.orm import backref
from sqlmodel import SQLModel, Field


# setup for SQLmodels
class bit_data(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bit_size: int = Field(default=0, nullable=False)
    bit_type: str = Field(default="", nullable=False)
    mfg: str = Field(default="", backref="manufacturer", nullable=False)
    serial_no: str = Field(default="")
    depth_in: float = Field(default=0.0)
    depth_out: float = Field(default=0.0)
    distance: float = Field(default=0.0)
    hours: float = Field(default=0.0)
    rop: float = Field(default=0.0)
    inner: int = Field(default=0)
    outer: int = Field(default=0)
    main: str = Field(default="")
    loc: str = Field(default="")
    bearing: str = Field(default="X")
    gauge: float = Field(default=0.0)
    other: str = Field(default="")
    reason_pulled: str = Field(default="")
    

class well_data(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    well_name: str = Field(default="")
    operator: str = Field(default="")
    lat: float = Field(default=0.0)
    lon: float = Field(default=0.0)


class manufacturer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    mfg_name: str = Field(default="")
