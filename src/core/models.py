import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Uuid, Boolean, String, ForeignKey

from config.database import Base
from src.core.constants import BaseModelConstants, BaseMediaModelConstants, AreaConstants


class IsDeletedFieldMixin:
    is_deleted = Column(Boolean, default=False)


class NameFieldMixin:
    name = Column(String(length=BaseModelConstants.NAME_MAX_LENGTH), nullable=False)


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(Uuid, default=uuid.uuid4, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BaseMediaModel(BaseModel):
    __abstract__ = True

    filename = Column(String(length=BaseMediaModelConstants.FILENAME_MAX_LENGTH), nullable=False)
    original_filename = Column(String(length=BaseMediaModelConstants.ORIGINAL_FILENAME_MAX_LENGTH), nullable=False)
    size = Column(Integer, nullable=False)
    mimetype = Column(String(length=BaseMediaModelConstants.MIMETYPE_MAX_LENGTH), nullable=False)


class Country(NameFieldMixin, BaseModel):
    __tablename__ = "country"


class Area(NameFieldMixin, BaseModel):
    __tablename__ = "area"

    country_id = Column(Integer, ForeignKey(Country.id), nullable=False)
    cardinal_direction_type = Column(
        String(length=AreaConstants.CARDINAL_DIRECTION_TYPE_MAX_LENGTH), nullable=False
    )


class City(NameFieldMixin, BaseModel):
    __tablename__ = "city"

    country_id = Column(Integer, ForeignKey(Country.id), nullable=False)
    area_id = Column(Integer, ForeignKey(Area.id), nullable=False)
