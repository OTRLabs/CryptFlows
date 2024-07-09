from sqlalchemy import create_engine, Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from ....configs.config import Config
#Base = declarative_base()
#engine = create_engine(f"{Config.SQLITE_DB_PATH}", echo=True)
