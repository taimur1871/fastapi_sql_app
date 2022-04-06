# define response models for end points
from pydantic import BaseModel
from typing import List, Optional


class LandingPage(BaseModel):
    name: str
    version: str
    description: str

    class Config:
        orm_model = True


# keeping some optional for testing purposes
class BitInfo(BaseModel):
    name: Optional[str]
    type: Optional[str]
    size: float
    sn: str
    well_name: str
    depth_in: Optional[float]
    depth_out: Optional[float]
    hours: Optional[float]
    num_blades: Optional[int]

    class Config:
        orm_model = True


# upload model
class UploadFiles(BaseModel):
    files: List[str]

    class Config:
        orm_model = True
