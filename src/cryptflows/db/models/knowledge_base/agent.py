from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ...database import KnowledgeBaseBase
class Agent(KnowledgeBaseBase):
    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    url: Mapped[str | None] = mapped_column(String(500), nullable=True) 

    def __repr__(self) -> str:
        return f"<Agent {self.name}>"