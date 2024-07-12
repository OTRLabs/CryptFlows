from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ...database import KnowledgeBaseBase


class File(KnowledgeBaseBase):
    __tablename__ = "file"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    path: Mapped[str] = mapped_column(String(255))
    sha256: Mapped[str] = mapped_column(String(255))
    size: Mapped[int] = mapped_column(Integer)
    file_type: Mapped[str] = mapped_column(String(255))