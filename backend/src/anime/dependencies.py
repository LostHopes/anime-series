from fastapi import HTTPException, Depends
from typing import Annotated
from sqlmodel import Session


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]