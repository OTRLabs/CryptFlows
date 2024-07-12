from __future__ import annotations


from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from litestar import Litestar, post
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

if TYPE_CHECKING:

    from sqlalchemy.ext.asyncio import AsyncSession


class Base(DeclarativeBase):
    pass