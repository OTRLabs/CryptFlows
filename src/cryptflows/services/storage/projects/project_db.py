from sqlalchemy import create_engine, Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from ....configs.config import Config
Base = declarative_base()
engine = create_engine(f"{Config.SQLITE_DB_PATH}", echo=True)

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    project_type = Column(Enum('Hack the Box', 'Bug Bounty', 'Red Team', 'Penetration Test', 'Security Compliance', name='project_types'), nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    scope = Column(String)
    end_date = Column(DateTime)
    status = Column(Enum('Planned', 'In Progress', 'Completed', name='project_statuses'), default='Planned')
    description = Column(String)

