from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String, Float, Numeric

from src.advertisements.constants import AdvertisementConstants
from src.core.constants import NUMERIC_PLACES, NUMERIC_MAX_DIGITS
from src.core.models import BaseModel, BaseFileModel, NameFieldMixin, IsDeletedFieldMixin, Country, Area, City
from src.users.models import User


class VehicleType(IsDeletedFieldMixin, NameFieldMixin, BaseModel):
    __tablename__ = "vehicle_type"


class VehicleBodyType(IsDeletedFieldMixin, NameFieldMixin, BaseModel):
    __tablename__ = "vehicle_body_type"

    vehicle_type_id = Column(Integer, ForeignKey(VehicleType.id), nullable=False)


class Manufacturer(IsDeletedFieldMixin, NameFieldMixin, BaseModel):
    __tablename__ = "manufacturer"


class Model(IsDeletedFieldMixin, NameFieldMixin, BaseModel):
    __tablename__ = "model"

    manufacturer_id = Column(Integer, ForeignKey(Manufacturer.id), nullable=False)
    production_start_year = Column(DateTime, nullable=True)
    production_end_year = Column(DateTime, nullable=True)
    is_still_in_production = Column(Boolean, default=False, nullable=True)


class Advertisement(IsDeletedFieldMixin, BaseModel):
    __tablename__ = "advertisement"

    author_id = Column(Integer, ForeignKey(User.id), nullable=False)

    vehicle_type_id = Column(Integer, ForeignKey(VehicleType.id), nullable=False)
    vehicle_body_type_id = Column(Integer, ForeignKey(VehicleBodyType.id), nullable=False)
    manufacturer_id = Column(Integer, ForeignKey(Manufacturer.id), nullable=False)
    model_id = Column(Integer, ForeignKey(Model.id), nullable=False)

    transmission = Column(String(length=AdvertisementConstants.TRANSMISSION_MAX_LENGTH), nullable=False)
    drive = Column(String(length=AdvertisementConstants.DRIVE_MAX_LENGTH), nullable=False)
    fuel = Column(String(length=AdvertisementConstants.FUEL_MAX_LENGTH), nullable=False)
    mileage = Column(Integer, nullable=False)
    production_year = Column(Integer, nullable=False)
    color = Column(String(length=AdvertisementConstants.COLOR_MAX_LENGTH), nullable=False)
    description = Column(String(length=AdvertisementConstants.DESCRIPTION_MAX_LENGTH), nullable=False)

    registration_country_id = Column(Integer, ForeignKey(Country.id), nullable=False)
    country_id = Column(Integer, ForeignKey(Country.id), nullable=False)
    area_id = Column(Integer, ForeignKey(Area.id), nullable=False)
    city_id = Column(Integer, ForeignKey(City.id), nullable=False)
    vin = Column(String(length=AdvertisementConstants.VIN_MAX_LENGTH), nullable=True)
    was_in_accident = Column(Boolean, nullable=False)

    bargain = Column(Boolean, nullable=False)
    exchange = Column(Boolean, nullable=False)
    condition = Column(String(length=AdvertisementConstants.CONDITION_MAX_LENGTH), nullable=False)
    manufacture_country_id = Column(Integer, ForeignKey(Country.id), nullable=True)
    fuel_consumption = Column(Float, nullable=False)
    engine_volume = Column(Float, nullable=False)
    engine_power = Column(Integer, nullable=False)
    headlights = Column(String(length=AdvertisementConstants.HEADLIGHTS_MAX_LENGTH), nullable=True)
    interior_material = Column(String(length=AdvertisementConstants.INTERIOR_MATERIAL_MAX_LENGTH), nullable=True)
    seat_adjustment = Column(String(length=AdvertisementConstants.SEAT_ADJUSTMENT_MAX_LENGTH), nullable=True)
    steering_wheel_adjustment = Column(String(length=AdvertisementConstants.STEERING_WHEEL_ADJUSTMENT_MAX_LENGTH), nullable=True)
    power_steering = Column(String(length=AdvertisementConstants.POWER_STEERING_MAX_LENGTH), nullable=True)
    heated_seats = Column(Boolean, nullable=False)
    heated_steering_wheel = Column(Boolean, nullable=False)
    heated_windshield = Column(Boolean, nullable=False)
    heated_rear_windshield = Column(Boolean, nullable=False)
    seat_ventilation = Column(Boolean, nullable=False)
    conditioner = Column(Boolean, nullable=False)
    window_lifters = Column(Boolean, nullable=False)
    configuration = Column(String(length=AdvertisementConstants.CONFIGURATION_MAX_LENGTH), nullable=False)
    count_owners = Column(Integer, nullable=False)

    price_usd = Column(Numeric(precision=NUMERIC_MAX_DIGITS, scale=NUMERIC_PLACES), nullable=True)


class AdvertisementMedia(BaseFileModel):
    __tablename__ = "advertisement_media"

    advertisement_id = Column(Integer, ForeignKey(Advertisement.id), nullable=False)


class AdvertisementFavourite(BaseModel):
    __tablename__ = "advertisement_favourite"

    advertisement_id = Column(Integer, ForeignKey(Advertisement.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
