from __future__ import annotations

from cryptflows.app import create_workflows_app, initialize_application_services
#from litestar import Litestar
# Uncomment the following lines if this script is to be run directly
if __name__ == "__main__":
    initialize_application_services()
    create_workflows_app("example_scope")