from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import Table, Column, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ...database import KnowledgeBaseBase
from .event_tag import EventTag, _event_tag


_event_tag = Table(
    'event_tag',
    KnowledgeBaseBase.metadata,
    Column('event_id', ForeignKey('event.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True)
)


class DocumentTag(KnowledgeBaseBase):
    __tablename__ = "event_tag"
    event_id = Column(ForeignKey("event.id"), primary_key=True)
    tag_id = Column(ForeignKey("tag.id"), primary_key=True)