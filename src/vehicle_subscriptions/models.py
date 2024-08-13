from sqlalchemy import Column, Integer, ForeignKey, Float, String, Boolean

from src.advertisements.constants import AdvertisementConstants
from src.advertisements.models import Model, Manufacturer, VehicleBodyType, VehicleType
from src.core.models import BaseModel, Area
from src.users.models import User


class VehicleSubscription(BaseModel):
    __tablename__ = "vehicle_subscription"

    subscriber_id = Column(Integer, ForeignKey(User.id), nullable=False)
    is_active = Column(Boolean, nullable=False)

    vehicle_type_id = Column(Integer, ForeignKey(VehicleType.id), nullable=False)
    vehicle_body_type_id = Column(Integer, ForeignKey(VehicleBodyType.id), nullable=False)
    manufacturer_id = Column(Integer, ForeignKey(Manufacturer.id), nullable=False)
    model_id = Column(Integer, ForeignKey(Model.id), nullable=False)

    transmission = Column(String(length=AdvertisementConstants.TRANSMISSION_MAX_LENGTH), nullable=True)
    drive = Column(String(length=AdvertisementConstants.DRIVE_MAX_LENGTH), nullable=True)
    fuel = Column(String(length=AdvertisementConstants.FUEL_MAX_LENGTH), nullable=True)
    engine_volume = Column(Float, nullable=True)
    production_start_year = Column(Integer, nullable=True)
    production_end_year = Column(Integer, nullable=True)
    area_id = Column(Integer, ForeignKey(Area.id), nullable=True)
