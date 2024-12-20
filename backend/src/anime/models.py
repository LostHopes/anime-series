from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    SecretStr,
    PositiveInt
)
from typing import List, Optional
from datetime import date, datetime
from enum import IntFlag
from sqlmodel import SQLModel, create_engine


class Role(IntFlag):
    USER = 0
    MODERATOR = 1
    ADMIN = 2


class User(BaseModel):
    id: PositiveInt = Field(description="Id of the user")
    username: str = Field(description="Username of the user")
    email: EmailStr = Field(description="User email")
    password: SecretStr = Field(description="The password of the user", exclude=True)
    age: PositiveInt = Field(description="User age")
    role: Role = Field(description="The role of the user", default=Role.USER)
    registered_date: datetime = Field(description="Date of the user registration")
    last_login: datetime = Field(description="Date of the user last login")
    animes: List['Anime'] = Field(default=[], description="User's collection of anime")


class AnimeDiscussion(BaseModel):
    id: PositiveInt = Field(description="Id of the anime discussion")
    title: str = Field(description="Title of the anime discussion")
    date_written: datetime = Field(description="Date of the creation anime discussion")
    users: List[User] = Field(default=[], description="Users participated in the discussion")
    last_message: datetime = Field(description="Last message of the anime discussion")


class Anime(BaseModel):
    id: PositiveInt = Field(description="Id of anime")
    eng_name: str = Field(description="English name of anime")
    ja_name: str = Field(description="Japanese name of anime")
    date_out: date = Field(description="Date of the first episode of the anime")
    date_completed: Optional[date] = Field(default=None, description="Date finished airing")
    status: str = Field(description="Status of anime")
    discussions: List[AnimeDiscussion] = Field(default=[], description="Discussions about the anime")


class UserMessage(BaseModel):
    id: PositiveInt = Field(description="Id of the user message")
    message: str = Field(description="The message itself")
    message_time: datetime = Field(description="Time when the message was sent")
    sender: User = Field(description="Sender of the message")
    discussion: AnimeDiscussion = Field(description="Discussion related to the user message")


database_url = "sqlite:///anime.db"
engine = create_engine(database_url)

def create_db():
    SQLModel.metadata.create_all(engine)
