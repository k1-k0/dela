from datetime import datetime, timedelta

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine

from dela.types import Status


class Base(DeclarativeBase): ...


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User[id={self.id!r}, name={self.name!r}]"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(2048))
    status: Mapped[Status] = mapped_column(default=Status.TODO)
    description: Mapped[str | None]
    start_date: Mapped[datetime | None]
    end_date: Mapped[datetime | None]
    duration: Mapped[timedelta | None]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task[id={self.id!r}, title={self.title!r}, status={self.status!r}]"


engine = create_engine("postgresql+psycopg://test:test@localhost:5432/dela", echo=True)
