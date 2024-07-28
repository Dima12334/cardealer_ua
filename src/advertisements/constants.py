from enum import Enum


class AdvertisementConstants:
    DESCRIPTION_MAX_LENGTH = 5000
    VIN_MAX_LENGTH = 17

    TRANSMISSION_MAX_LENGTH = 1
    DRIVE_MAX_LENGTH = 1
    FUEL_MAX_LENGTH = 1
    COLOR_MAX_LENGTH = 1
    CONDITION_MAX_LENGTH = 1
    HEADLIGHTS_MAX_LENGTH = 1
    INTERIOR_MATERIAL_MAX_LENGTH = 1
    SEAT_ADJUSTMENT_MAX_LENGTH = 1
    STEERING_WHEEL_ADJUSTMENT_MAX_LENGTH = 1
    POWER_STEERING_MAX_LENGTH = 1
    CONFIGURATION_MAX_LENGTH = 1

    class TransmissionEnum(str, Enum):
        pass

    class DriveEnum(str, Enum):
        pass

    class FuelEnum(str, Enum):
        pass

    class ColorEnum(str, Enum):
        pass

    class ConditionEnum(str, Enum):
        pass

    class HeadlightsEnum(str, Enum):
        pass

    class InteriorMaterialEnum(str, Enum):
        pass

    class SeatAdjustmentEnum(str, Enum):
        pass

    class SteeringWheelAdjustmentEnum(str, Enum):
        pass

    class PowerSteeringEnum(str, Enum):
        pass

    class ConfigurationEnum(str, Enum):
        pass
