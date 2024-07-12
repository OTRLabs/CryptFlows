from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ...database import KnowledgeBaseBase
from .event_tag import EventTag, _event_tag

class Event(KnowledgeBaseBase):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    tags: Mapped[list[EventTag]] = relationship(
        secondary=lambda: _event_tag(),
        back_populates="events",
    )

    def __repr__(self):
        return f"Event(id={self.id}, name={self.name})"
    