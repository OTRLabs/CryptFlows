from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ...database import KnowledgeBaseBase
from .document_tag import DocumentTag, _document_tag

class Document(KnowledgeBaseBase):
    name: Mapped[str] = mapped_column(String(length=255), index=True)
    description: Mapped[str | None] = mapped_column(String(length=255), index=False, nullable=True)
    tags: Mapped[list[DocumentTag]] = relationship(
        secondary=lambda: _document_tag(),
        back_populates="documents",
    )

    def __repr__(self) -> str:
        return f"<Document {self.name}>"