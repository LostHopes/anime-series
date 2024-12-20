from datetime import date, datetime
from enum import IntFlag
from typing import List, Optional

from fastapi import FastAPI, Depends
from pydantic import EmailStr, Field, PositiveInt, SecretStr
from sqlmodel import Field, Relationship, SQLModel, create_engine


class Role(IntFlag):
    USER = 0
    MODERATOR = 1
    ADMIN = 2


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(description="Username of the user", index=True)
    email: EmailStr = Field(description="User email", unique=True)
    password: str = Field(description="The password of the user")  # SecretStr cannot be used here
    age: PositiveInt = Field(description="User age")
    role: Role = Field(default=Role.USER, description="The role of the user")
    registered_date: datetime = Field(default_factory=datetime.utcnow, description="Date of registration")
    last_login: datetime = Field(default_factory=datetime.utcnow, description="Date of last login")
    

    animes: List["Anime"] = Relationship(back_populates="owner")


class Anime(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    eng_name: str = Field(description="English name of anime", index=True)
    ja_name: str = Field(description="Japanese name of anime")
    date_out: date = Field(description="Date of the first episode of the anime")
    date_completed: Optional[date] = Field(default=None, description="Date finished airing")
    status: str = Field(description="Status of anime")
    

    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    owner: Optional[User] = Relationship(back_populates="animes")
    discussions: List["AnimeDiscussion"] = Relationship(back_populates="anime")


class AnimeDiscussion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(description="Title of the anime discussion")
    date_written: datetime = Field(default_factory=datetime.utcnow, description="Creation date")
    last_message: datetime = Field(default_factory=datetime.utcnow, description="Last message time")
    
    anime_id: Optional[int] = Field(default=None, foreign_key="anime.id")
    anime: Optional[Anime] = Relationship(back_populates="discussions")
    messages: List["UserMessage"] = Relationship(back_populates="discussion")


class UserMessage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str = Field(description="The message itself")
    message_time: datetime = Field(default_factory=datetime.utcnow, description="Message timestamp")
    
    sender_id: Optional[int] = Field(default=None, foreign_key="user.id")
    sender: Optional[User] = Relationship()
    discussion_id: Optional[int] = Field(default=None, foreign_key="animediscussion.id")
    discussion: Optional[AnimeDiscussion] = Relationship(back_populates="messages")


database_url = "sqlite:///anime.db"
engine = create_engine(database_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)