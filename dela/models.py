from datetime import datetime, timedelta
from pydantic import BaseModel, Field

from dela.types import Status


class User(BaseModel):
    name: str
    tasks: list["Task"]


class Task(BaseModel):
    title: str = Field(max_length=2048)
    status: Status
    description: str | None
    start_date: datetime | None
    end_date: datetime | None
    duration: timedelta | None
