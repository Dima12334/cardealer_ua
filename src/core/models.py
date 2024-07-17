import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Uuid, Boolean, String, ForeignKey

from config.database import Base
from src.core.constants import BaseModelConstants, AreaConstants


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(type_=Uuid, default=uuid.uuid4, unique=True, index=True)
    created_at = Column(type_=DateTime, default=datetime.utcnow)
    updated_at = Column(type_=DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(type_=Boolean, default=False)


class BaseNameModel(BaseModel):
    name = Column(type_=String(length=BaseModelConstants.NAME_MAX_LENGTH), nullable=False)


class Country(BaseNameModel):
    __tablename__ = "country"


class Area(BaseNameModel):
    __tablename__ = "area"

    country_id = Column(Integer, ForeignKey(Country.c.id), nullable=False)
    cardinal_direction_type = Column(type_=String(length=AreaConstants.CARDINAL_DIRECTION_TYPE_MAX_LENGTH), nullable=False)


class City(BaseNameModel):
    __tablename__ = "city"

    country_id = Column(Integer, ForeignKey(Country.c.id), nullable=False)
    area_id = Column(Integer, ForeignKey(Area.c.id), nullable=False)
