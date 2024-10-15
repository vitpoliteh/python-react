import uuid
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy import UUID, DateTime
from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Column, Table
from datetime import datetime


class Base(DeclarativeBase):
    ...

class UUIDBase(Base):
    __abstract__ = True
    id: Mapped[uuid.UUID] = mapped_column(UUID, nullable=False, primary_key=True)


class UUIDAuditBase(UUIDBase):
    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
