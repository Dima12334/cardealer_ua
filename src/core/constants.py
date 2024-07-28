from enum import Enum


NUMERIC_MAX_DIGITS = 10
NUMERIC_PLACES = 2


class BaseModelConstants:
    NAME_MAX_LENGTH = 255


class BaseMediaModelConstants:
    FILENAME_MAX_LENGTH = 255
    ORIGINAL_FILENAME_MAX_LENGTH = 255
    MIMETYPE_MAX_LENGTH = 255


class AreaConstants:
    CARDINAL_DIRECTION_TYPE_MAX_LENGTH = 5

    class CardinalDirectionTypeEnum(str, Enum):
        SOUTH = "SOUTH"
        EAST = "EAST"
        NORTH = "NORTH"
        WEST = "WEST"
