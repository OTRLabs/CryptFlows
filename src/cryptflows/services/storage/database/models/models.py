from __future__ import annotations
from advanced_alchemy.base import UUIDBase
from advanced_alchemy.filters import LimitOffset
from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy import create_engine
from advanced_alchemy.config.sync import SQLAlchemySyncConfig
from typing import TYPE_CHECKING
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped, Session, sessionmaker

from advanced_alchemy.base import UUIDBase
from advanced_alchemy.filters import LimitOffset
from advanced_alchemy.repository import SQLAlchemySyncRepository
from advanced_alchemy.utils.fixtures import open_fixture
from .....configs.config import Config

# Define your base model

# Define your models

DuckDBBase = SQLAlchemySyncConfig.create_engine_callable = lambda: create_engine(f"duckdb:///{Config.DUCKDB_PATH}")


class Project(UUIDBase):
    __tablename__ = 'projects'
    
    id = Column(Integer, Sequence('project_id_seq'), primary_key=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(String, nullable=False)
    end_date = Column(String)
    status = Column(String)
    scope = Column(String)
class Task(UUIDBase):
    __tablename__ = 'tasks'
    
    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    project_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    completed = Column(Integer)

# Repositories for the models
class ProjectRepository(SQLAlchemySyncRepository[Project]):
    model_type = Project

class TaskRepository(SQLAlchemySyncRepository[Task]):
    model_type = Task
