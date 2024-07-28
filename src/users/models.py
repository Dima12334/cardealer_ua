from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, DateTime

from src.core.models import BaseModel, IsDeletedFieldMixin
from .constants import UserConstants


class User(IsDeletedFieldMixin, BaseModel):
    __tablename__ = "user"

    first_name = Column(String(length=UserConstants.FIRST_NAME_MAX_LENGTH), nullable=False)
    middle_name = Column(String(length=UserConstants.MIDDLE_NAME_MAX_LENGTH), nullable=True)
    last_name = Column(String(length=UserConstants.LAST_NAME_MAX_LENGTH), nullable=False)
    username = Column(String(length=UserConstants.USERNAME_MAX_LENGTH), nullable=False, unique=True)

    phone_number = Column(String(length=UserConstants.PHONE_NUMBER_MAX_LENGTH), nullable=True)
    email = Column(String(length=UserConstants.EMAIL_MAX_LENGTH), nullable=False, unique=True)
    password = Column(String(length=UserConstants.PASSWORD_MAX_LENGTH), nullable=False)
    avatar = Column(String(length=UserConstants.AVATAR_MAX_LENGTH), nullable=True)
    user_type = Column(String(length=UserConstants.USER_TYPE_MAX_LENGTH), nullable=False)

    last_login = Column(DateTime, nullable=True)
    last_online = Column(DateTime, nullable=True)
    is_online = Column(Boolean, nullable=True)
    count_all_advertisements = Column(Integer, nullable=False, default=0)


class UserRating(BaseModel):
    __tablename__ = "user_rating"

    rating = Column(Integer, nullable=False)
    user_to_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user_from_id = Column(Integer, ForeignKey(User.id), nullable=False)
