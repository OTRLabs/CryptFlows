from __future__ import annotations

from litestar.app import Litestar

from cryptflows.app import create_app

def main() -> None:
    app = create_app()
    app.run()



if __name__ == "__main__":
    main()