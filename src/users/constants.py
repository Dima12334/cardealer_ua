from enum import Enum


class UserConstants:
    FIRST_NAME_MAX_LENGTH = 150
    MIDDLE_NAME_MAX_LENGTH = 150
    LAST_NAME_MAX_LENGTH = 150
    USERNAME_MAX_LENGTH = 150

    PHONE_NUMBER_MAX_LENGTH = 13
    AVATAR_MAX_LENGTH = 2048
    USER_TYPE_MAX_LENGTH = 9

    EMAIL_MAX_LENGTH = 254
    PASSWORD_MAX_LENGTH = 128

    class UserTypeEnum(str, Enum):
        DEFAULT = "DEFAULT"
        MODERATOR = "MODERATOR"
        ADMIN = "ADMIN"


class UserRatingConstants:

    class RatingNumberEnum(int, Enum):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
