from datetime import date

from fastapi import UploadFile, Form, File, HTTPException
from pydantic import BaseModel, field_validator, HttpUrl

from src.validation import (
    validate_name,
    validate_image,
    validate_gender,
    validate_birth_date,
)


class UserProfileSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    avatar: UploadFile
    gender: str
    date_of_birth: date
    info: str

    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, value: str):
        validate_name(value)

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, value: str):
        validate_name(value)

    @field_validator("avatar")
    @classmethod
    def validate_avatar_image(cls, value: UploadFile):
        validate_image(value)

    @field_validator("gender")
    @classmethod
    def validate_profile_gender(cls, value: str):
        validate_gender(value)

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value: date):
        validate_birth_date(value)


class GroupSchema:
    pass


class UserSchema(BaseModel):
    id: int
    email: str
    _hashed_password: str
    is_active: bool
    created_at: date
    updated_at: date
    group_id: int
    group: list[GroupSchema]
    activation_token: str
    password_reset_token: str
    refresh_tokens: str
    profile: UserProfileSchema


class UserCreate(UserSchema):
    pass
