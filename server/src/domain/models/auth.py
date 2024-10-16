from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String
from .base import UUIDBase


class BaseUser(UUIDBase):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )
    password: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )
