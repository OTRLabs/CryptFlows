from __future__ import annotations

from typing import TYPE_CHECKING
from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .team import Team
    from ..team.team_member import TeamMember

#from import Base
from sqlalchemy import Table, Column, ForeignKey

def _team_proxy():
    return Table(
        "proxy_team",
        Base.metadata,
        Column("proxy_id", ForeignKey("proxy.id"), primary_key=True),
        Column("team_id", ForeignKey("team.id"), primary_key=True),
    )

class Proxy(UUIDAuditBase):

    __tablename__ = "proxy"
    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str | None] = mapped_column(String(length=500), index=False, nullable=True)
    teams: Mapped[list[Team]] = relationship(
        secondary=lambda: _team_proxy(),
        back_populates="proxies",
    )
    members: Mapped[list[TeamMember]] = relationship(
        secondary=lambda: _team_member_proxy(),
        back_populates="proxies",