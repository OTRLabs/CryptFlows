from .project_db import Session, Project
from datetime import datetime


from typing import List

def list_available_projects() -> List[Project]:
    """
    This function lists all available projects in the database.

    :return: List of Project objects
    """
    session = Session()

    projects = session.query(Project).all()

    return projects

from .project_db import Session, Project
from datetime import datetime
from typing import List

def create_new_project(project_name: str) -> None:
    """
    Create a new project in the database.

    :param project_name: str, the name of the project
    :return: None
    """
    session = Session()

    new_project: Project = Project(
        name=f"{project_name} - {datetime.now()}",
        project_type="Hack the Box",
        description="Beginner-friendly HTB machine for practice",
        status="In Progress"
    )

    session.add(new_project)
    session.commit()

    projects: List[Project] = session.query(Project).all()
    for project in projects:
        print(f"Project: {project.name}, Type: {project.project_type}, Status: {project.status}")

    # Close the session
    session.close()
