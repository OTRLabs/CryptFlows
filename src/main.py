from __future__ import annotations
from cryptflows.app import create_workflows_app
from cryptflows.services.workflows.project_management.project_utils import Project
from datetime import datetime
from rich.console import Console, Theme
from rich.prompt import Prompt
import csv
from cryptflows.cli.repl.repl_utils import COMMANDS
from cryptflows.cli.repl.repl_handlers import CryptFlowsREPL, init_repl
from advanced_alchemy.repository import SQLAlchemySyncRepository
from cryptflows.services.storage.database.db import DatabaseUtils
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cryptflows.configs.config import Config
from cryptflows.services.storage.database.models.models import Base
from cryptflows.tui.terminal_user_interface import CryptFlowsApp


if __name__ == "__main__":
    app = CryptFlowsApp()
    app.run()