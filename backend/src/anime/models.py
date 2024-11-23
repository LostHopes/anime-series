from datetime import datetime, date
from pydantic import BaseModel, validator
from typing import Optional


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
    email: str
    password: str
    age: int

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


