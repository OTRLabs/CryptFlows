from __future__ import annotations

from cryptflows.app import create_workflows_app
#from litestar import Litestar

workflows_app = create_workflows_app()

#app = Litestar()

def main():
    workflows_app.run()


if __name__ == "__main__":
    main()