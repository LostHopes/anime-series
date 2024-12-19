from pydantic import (
    BaseModel,
    validator,
    EmailStr,
    Field,
    SecretStr,
    PositiveInt,
    date,
    datetime
)
from typing import Optional
from enum import IntFlag


class Role(IntFlag):
    USER = 0
    MODERATOR = 1
    ADMIN = 2


class AnimeDiscussion(BaseModel):
    id: PositiveInt = Field("Id of the anime discussion")
    title: str = Field(description="Title of the anime discussion")
    date_written: datetime = Field(description="Date of the creation anime discussion")
    users: list[User] = Field("Users participated in the discussion")
    last_message: datetime = Field("Last message of the anime discussion")


class Anime(BaseModel):
    id: PositiveInt = Field(description="Id of anime")
    eng_name: str = Field(description="English name of anime")
    ja_name: str = Field(description="Japanese name of anime")
    date_out: date = Field("Date of the first episode of the anime")
    date_completed = Field("Date finished airing")
    status: str = Field(description="Status of anime")
    discussions: AnimeDiscussion = Field(description="Discussion of anime")


class User(BaseModel):
    id: PositiveInt = Field("Id of the user")
    username: str = Field(description="Username of the user")
    email: EmailStr = Field(description="User email")
    password: SecretStr = Field(description="The password of the user", exclude=True)
    age: PositiveInt = Field(description="User age")
    role: Role = Field(description="The role of the user", default=Role.USER)
    animes: list[Anime] = Field("User's collection of anime")
    registered_date: datetime = Field("Date of the user registration")
    last_login: datetime = Field("Date of the user last login")


class UserMessage(BaseModel):
    id: PositiveInt = Field("Id of the user message")
    message: str = Field("The message itself")
    message_time: datetime = Field(description="Message of the user message")
    sender: User = Field("Sender of the message")
    discussion: AnimeDiscussion = Field("Discussion of the user message")

