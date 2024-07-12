from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from advanced_alchemy.base import UUIDAuditBase


class Agent(UUIDAuditBase):
    name