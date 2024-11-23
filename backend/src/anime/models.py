from datetime import datetime, date
from pydantic import (
    BaseModel,
    validator,
    EmailStr,
    Field,
    SecretStr
)
from typing import Optional
from enum import IntFlag


class Role(IntFlag):
    USER = 0
    MODERATOR = 1
    ADMIN = 2


class Anime(BaseModel):
    id: int
    eng_name: str
    ja_name: str
    date_out: date
    status: str
    discussions: AnimeDiscussion


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: SecretStr = Field(description="The password of the user", exclude=True)
    age: int
    role: Role = Field(description="The role of the user", default=Role.USER)

    animes: list[Anime]
    registered_date: datetime = datetime.now().replace(second=0, microsecond=0)
    last_login: datetime


class UserMessage(BaseModel):
    pass


class AnimeDiscussion(BaseModel):
    id: int
    name: str

    users: list[User]
    last_message: datetime


