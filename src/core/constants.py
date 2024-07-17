from enum import Enum


class BaseModelConstants:
    NAME_MAX_LENGTH = 255


class AreaConstants:
    CARDINAL_DIRECTION_TYPE_MAX_LENGTH = 5

    class CardinalDirectionTypeEnum(str, Enum):
        SOUTH = "SOUTH"
        EAST = "EAST"
        NORTH = "NORTH"
        WEST = "WEST"
