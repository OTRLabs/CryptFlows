from __future__ import annotations
from rich.console import Console
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import Engine
from ....configs.config import Config
from .models.models import Base, Project, Task

class DatabaseUtils:
    def __init__(self, console: Console) -> None:
        self.console = console
        self.console.print("Initializing database...", style="bold green")
        self.engine: Engine = self.connect_to_database()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.init_db()

    def connect_to_database(self) -> Engine:
        """
        Connect to the SQLite database and return the engine.
        Returns:
            Engine: The SQLAlchemy database engine.
        """
        engine: Engine = create_engine(
            f"sqlite:///{Config.SQLITE_DB_PATH}",
        )
        return engine

    def get_session(self) -> Session:
        """
        Create a new SQLAlchemy session.
        Returns:
            Session: A new SQLAlchemy session.
        """
        return self.SessionLocal()

    def init_db(self, engine: Engine) -> None:
        """
        Initialize the database by creating tables.
        """
        Base.metadata.create_all(bind=self.engine)

    def add_project(self, name: str, description: str, start_date: str, end_date: str, status: str, scope: str) -> None:
        """
        Add a new project to the database.
        """
        session = self.get_session()
        new_project = Project(name=name, description=description, start_date=start_date, end_date=end_date, status=status, scope=scope)
        session.add(new_project)
        session.commit()
        session.close()

    def get_projects(self) -> list[Project]:
        """
        Get all projects from the database.
        Returns:
            list[Project]: List of all projects.
        """
        session = self.get_session()
        projects = session.query(Project).all()
        session.close()
        return projects

    def add_task(self, project_id: int, title: str, description: str, completed: int = 0) -> None:
        """
        Add a new task to a project.
        """
        session = self.get_session()
        new_task = Task(project_id=project_id, title=title, description=description, completed=completed)
        session.add(new_task)
        session.commit()
        session.close()

    def get_tasks_for_project(self, project_id: int) -> list[Task]:
        """
        Get all tasks for a specific project.
        Returns:
            list[Task]: List of tasks for the project.
        """
        session = self.get_session()
        tasks = session.query(Task).filter(Task.project_id == project_id).all()
        session.close()
        return tasks
